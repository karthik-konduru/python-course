#Social Media Application using Abstraction
from abc import ABC, abstractmethod
class Common_Features(ABC):
    @abstractmethod
    def Messanger(self):
        pass
    @abstractmethod
    def Calls(self):
        pass
    @abstractmethod
    def Search(self):
        pass
    @abstractmethod
    def Settings(self):
        pass
class Instagram(Common_Features):
    def reels(self):
        print('Scrolling Reels')
    def Post(self):
        print('Posting in Instagram')
    def Comments(self):
        print('Commenting')
    def Followers(self):
        print('Followers')
    def Story(self):
        print('Story')
    def Messanger(self):
        print('Messaging')
    def Calls(self):
        print('Insta Calling...')
    def Search(self):
        print('Instagram Searching...')
    def Settings(self):
        print('Instagram Open Settings')
    
class Whatsapp(Common_Features):
    def Updates(self):
        print('Updating Whatsapp')
    def Channels(self):
        print('Channels')
    def Status(self):
        print('Status')
    def Messanger(self):
        print('Messaging')
    def Calls(self):
        print('Whatsapp Calling...')
    def Search(self):
        print('Whatsapp Searching...')
    def Settings(self):
        print('Whatsapp Open Settings')
w=Whatsapp()
w.Updates()
w.Channels()
w.Status()
w.Messanger()
w.Calls()
w.Search()
w.Settings()

print()
i=Instagram()
i.reels()
i.Post()
i.Comments()
i.Followers()
i.Story()
i.Messanger()
i.Calls()
i.Search()
i.Settings()