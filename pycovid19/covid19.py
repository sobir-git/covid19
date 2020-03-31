from IPython.display import Javascript


class __Quarantine():
    puton_msg = "Yay! You and your notebook are safe now \N{grinning face}. Happy Quarantine!"
    takeoff_msg = "Sorry but you asked for it. Anyways, be careful going around without mask."

    def __init__(self):
        self.__protected_logo_web = "https://user-images.githubusercontent.com/34193118/77956617-da5a2800-72da-11ea-9b67-7dfce6af6569.png"
        self.__normal_logo = '/static/base/images/logo.png'
        self.__masked_agent_web = "https://user-images.githubusercontent.com/34193118/77957571-5bfe8580-72dc-11ea-83b4-2d0959e0ef82.png"

    def __change_logo(self, logo, msg):
        code = r'''var newsrc = "{logo}";
var img = document.querySelector("#ipython_notebook > a > img");
img.src = newsrc;
var msg = "{msg}";
var img = '<img style="display:inline" src="{masked_agent}">';
element.append(img);
element.append(msg);'''.format(msg=msg, masked_agent=self.__masked_agent_web, logo=logo)
        # print(repr(code))
        # print()
        # print(code)
        return Javascript(code)

    def protect_me(self):
        return self.__change_logo(self.__protected_logo_web, self.puton_msg)

    def i_am_suffocating(self):
        return self.__change_logo(self.__normal_logo, self.takeoff_msg)


quarantine = __Quarantine()

if __name__ == '__main__':
    quarantine.protect_me()
