# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        try:
            guid = entry.guid
            title = translate_html(entry.title)
            link = entry.link
            description = translate_html(entry.description)
            pubdate = translate_html(entry.published)

            try:
                pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
                pubdate.replace(tzinfo=pytz.timezone("GMT"))
            #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
            #  pubdate.replace(tzinfo=None)
            except ValueError:
                pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

            newsStory = NewsStory(guid, title, description, link, pubdate)
            ret.append(newsStory)
        except Exception as e:
            # print('Esta "entry" no es compatible o le falta informacion, la omito')
            pass
    return ret

#======================
# Data structure design
#======================

# Problem 1
class NewsStory(object):
    '''
    Objeto que contiene todos los atributos de una Noticia
    previamente "parseada" desde cualquier RSS feed
    '''
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description =  description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        '''
        Getter para acceder de manera de segura al identificador unico de 
        la noticia "guid"
        '''
        return self.guid

    def get_title(self):
        '''
        Getter para acceder de manera de segura al titulo de la noticia
        '''
        return self.title

    def get_description(self):
        '''
        Getter para acceder de manera de segura a la descripción de la noticia
        '''
        return self.description

    def get_link(self):
        '''
        Getter para acceder de manera de segura al enlace al articulo completo
        '''
        return self.link

    def get_pubdate(self):
        '''
        Getter para acceder de manera de segura a la información sobre la 
        fecha de publicación de la noticia
        '''
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# Problem 2: Phrase Triggers
class PhraseTrigger(Trigger):
    def is_phrase_in(self, phrase, text):
        '''
        Devuelve True si una alerta debiera ser generada
        para la "story" dada, o False en caso contrario.

        Se asume que la "phrase" no contiene signos de puntuación y
        cada palabra está separada por un unico espacio.

        Debe disparar sólo cuando todas las palabras de la "phrase" 
        aparecen y de manera consecutiva, separadas solo por "espacio"
        o signos de puntuación.

        NO debe ser "case sensitive"
        '''
        # debo preprocesar la "phrase" y el "text"
        # phrase: simplemente llevar a lower, ya que debe ser NO case-sensitive
        # text: eliminar signos de puntuación y espacios indebidos
        phrase = phrase.lower()
        phrase = ' ' + phrase + ' '

        text = text.lower()
        clean_text = re.sub(r"[,.;@#?!&$%]+\ *", " ", text)
        clean_text_list = clean_text.split()
        clean_text = ' ' + ' '.join(clean_text_list) + ' '

        # le agregue espacios al inicio y final 
        # para poder hacer el chequeo de la phrase exacta (no plurales)
        # sin tener que volver a hacer split() de text y phrase

        return phrase in clean_text


# Problem 3: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):        
        self.phrase = phrase

    def evaluate(self, story):
        '''
        Evalua si la "phrase" se encuentra en el "title" 
        de la "NewsStory
        '''
        return self.is_phrase_in(self.phrase, story.get_title())


# Problem 4: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        '''
        Evalua si la "phrase" se encuentra en la "description" 
        de la "NewsStory
        '''
        return self.is_phrase_in(self.phrase, story.get_description())


# TIME TRIGGERS
# Problem 5: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def sample():
        print('sample')
        return None


# Problem 6: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, date_time_string):
        self.date_time = datetime.strptime(date_time_string, "%d %b %Y %H:%M:%S")
    
    def evaluate(self, story):
        '''
        Devuelve True si la "story" ocurrió antes de la "date_time".

        Se asume "date_time" correspondiente a EST, y con formato "%d %b %Y %H:%M:%S". 
        (Pero no incluyo la "tzinfo" en mi date_time)
        '''
        # Debo preprocesar la fecha de la "story", para compatibilidad con la de mi Clase
        # date_time: aware/naiv (incluye o no informacion de la zona horaria)
        story_pubdate = story.get_pubdate()
        story_pubdate = story_pubdate.replace(tzinfo=None)
        return story_pubdate < self.date_time


class AfterTrigger(TimeTrigger):
    def __init__(self, date_time_string):
        self.date_time = datetime.strptime(date_time_string, "%d %b %Y %H:%M:%S")
    
    def evaluate(self, story):
        '''
        Devuelve True si la "story" ocurrió antes de la "date_time".

        Se asume "date_time" correspondiente a EST, y con formato "%d %b %Y %H:%M:%S". 
        (Pero no incluyo la "tzinfo" en mi date_time)
        '''        
        # Debo preprocesar la fecha de la "story", para compatibilidad con la de mi Clase
        # date_time: aware/naiv (incluye o no informacion de la zona horaria)
        story_pubdate = story.get_pubdate()
        story_pubdate = story_pubdate.replace(tzinfo=None)
        return story_pubdate > self.date_time


# COMPOSITE TRIGGERS
# Problem 7: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    
    def evaluate(self, story):
        '''
        Devolvera True si el "trigger" correspondiente NO dispararía 
        para esa "story".
        '''
        return not self.trigger.evaluate(story)


# Problem 8: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2
    
    def evaluate(self, story):
        '''
        Devolvera True solo si AMBOS "trigger"s dispararían para esa "story".
        '''        
        return self.t1.evaluate(story) and self.t2.evaluate(story)


# Problem 9: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2
    
    def evaluate(self, story):
        '''
        Devolvera True si AL MENOS 1 de los "trigger"s dispararían para esa "story".
        '''        
        return self.t1.evaluate(story) or self.t2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = [
        story
        for story in stories
        if any([ trigger.evaluate(story) for trigger in triggerlist ])
    ]
    # filtered_stories = stories
    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # Problem 11: build triggers
    # Tipos de triggers disponibles
    trigger_classes = { 
        'TITLE': TitleTrigger, 
        'DESCRIPTION': DescriptionTrigger,
        'AND': AndTrigger,
        'OR': OrTrigger,
        'NOT': NotTrigger,
        'BEFORE': BeforeTrigger,
        'AFTER': AfterTrigger,
    }

    # dict, cada trigger que voy creando:
    # key -> trigger_name, value -> trigger instance
    triggers_dict = {}
    triggerlist = []

    for command in lines:
        fields = command.split(',')
        if fields[0] != 'ADD':
            # Comando de creacion de un Trigger
            # Guardo en dict una instancia del trigger con t_name, t_type y los args
            t_name = fields[0]
            t_type = fields[1]
            if t_type in ['AND', 'OR']:
                # compose triggers
                t1 = triggers_dict[fields[2]]
                t2 = triggers_dict[fields[3]]
                triggers_dict[t_name] = trigger_classes[t_type](t1, t2)
            elif t_type in ['TITLE', 'DESCRIPTION', 'BEFORE', 'AFTER']:
                # phrase y time triggers
                arg = fields[2]
                triggers_dict[t_name] = trigger_classes[t_type](arg)
            elif t_type == 'NOT':
                # not trigger
                tx = triggers_dict[fields[2]]
                triggers_dict[t_name] = trigger_classes[t_type](tx)
            else:
                continue
        
        else:
            # Comando 'ADD' -> Agrega los triggers a la lista final
            # Los siguientes campos son los nombres de triggers a agregar
            for t_name in fields[1:]:
                triggerlist.append(triggers_dict[t_name])

    return triggerlist


# Programa principal
SLEEPTIME = 120 # seconds -- how often we poll

GOOGLE_NEWS_RSS = "http://news.google.com/news?output=rss"
YAHOO_NEWS_RSS = "http://news.yahoo.com/rss/topstories"

GOOGLE_NEWS_RSS_AR = "https://news.google.com/rss?hl=es-419&gl=AR&ceid=AR:es-419"
YAHOO_NEWS_RSS_AR = "https://espanol.yahoo.com/topics/noticias-de-argentina/"

def main_thread(master):
    try:
        # Sample triggerlist
        # t1 = TitleTrigger("election")
        # t2 = DescriptionTrigger("Trump")
        # t3 = DescriptionTrigger("Clinton")  
        # t4 = AndTrigger(t2, t3)
        # triggerlist = [t1, t4]

        # Problem 11: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers_boca_juniors.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title(), "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            # Get stories from Google's and Yahoo's Top Stories RSS news feed
            stories = process(GOOGLE_NEWS_RSS_AR)
            stories.extend(process(YAHOO_NEWS_RSS))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

