from IPython.display import Javascript


class __Quarantine():
    def __init__(self):
        self.__protected_logo = 'jupyter_logo.png'
        self.__normal_logo = '/static/base/images/logo.png'
        self.__masked_agent = 'masked_agent.png'

    def __change_logo(self, logo, agent=False):
        code = r'''var newsrc = "{logo}";
var img = document.querySelector("#ipython_notebook > a > img");
img.src = newsrc;
        '''.format(logo=logo)
        if agent:
            code += '''
var output = "<img src={masked_agent}>"
element.append(output);'''.format(masked_agent=self.__masked_agent)
        # print(repr(code))
        # print()
        # print(code)
        return Javascript(code)

    def protect_me(self):
        print("Yay! You and your notebook are safe now \N{grinning face}. Happy Quarantine!")
        return self.__change_logo(self.__protected_logo)

    def i_am_suffocating(self):
        print("Sorry but you asked for it. Anyways, be careful going around without mask.")
        return self.__change_logo(self.__normal_logo)


quarantine = __Quarantine()

__all__ = [quarantine]

if __name__ == '__main__':
    quarantine.protect_me()
