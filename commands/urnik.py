from urllib.request import urlopen as uRec
from bs4 import BeautifulSoup as soup
import discord
import random


def urnik_by_razred(selected_razred):
    urnik_url = "https://www.easistent.com/urniki/307dd36f0b3533186a238aa0411889e402ec7478/razredi/423682"
    #urnik_url = "https://www.easistent.com/urniki/12296fadef0fe622b9f04637b58002abc872259c/razredi/421675"
    uClient = uRec(urnik_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    try:
        razred_value = page_soup.find_all(
            "option", string=selected_razred)[0]["value"]
    except IndexError:
        try:
            selected_razred = selected_razred.split(".")
            selected_razred = str(
                selected_razred[0]) + ". " + str(selected_razred[1])
            razred_value = page_soup.find_all(
                "option", string=selected_razred)[0]["value"]
        except IndexError:
            selected_razred = selected_razred.lower()
            selected_razred = selected_razred.split(".")
            selected_razred = str(
                selected_razred[0]) + "." + str(selected_razred[1])
            razred_value = page_soup.find_all(
                "option", string=selected_razred)[0]["value"]

    urnik_url = f"https://www.easistent.com/urniki/307dd36f0b3533186a238aa0411889e402ec7478/razredi/{razred_value}"
    uClient = uRec(urnik_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    try:
        dan_urnika = page_soup.findAll(
            "th", {"class": "ednevnik-seznam_ur_teden-th-danes"})[0].text.strip().split("\n")
    except IndexError:
        embed = discord.Embed(title="Dons je viknd papak!", color=0xff0000)
        return embed

    dan_urnika = f"{dan_urnika[0]} {dan_urnika[1]}"

    današnji_dan = page_soup.findAll(
        "td", {"class": "ednevnik-seznam_ur_teden-td ednevnik-seznam_ur_teden-td-danes"})

    razred = page_soup.findAll("option", {"selected": "selected"})[
        1].text.strip()

    x = 1
    embed = discord.Embed(title=f":school:Gsšrm urnik {razred}:",
                          color=random.randint(0, 0xffffff))
    for ura in današnji_dan[1: len(današnji_dan)]:
        try:
            ure = page_soup.findAll("div", {"class": "text10 gray"})[
                x].text.strip()
            ura = današnji_dan[x].findAll("td", {"class": "text14"})
            ura = ura[0].text.strip()
            profesor_in_uč = današnji_dan[x].div.div.text.strip().split(",")
            profesor = profesor_in_uč[0]
            učilnica = profesor_in_uč[1]
            x += 1
            embed.add_field(name=f"{x-1}. {ura}:     {ure}",
                            value=f"-{profesor}     (uč. {učilnica})", inline=False)
        except AttributeError:
            pass
        except IndexError:
            pass

    embed.set_footer(text="Kamnik FTW😎")
    embed.set_author(
        name=dan_urnika, icon_url="https://cdn.discordapp.com/attachments/781881996430671912/784013894498385960/EISJtkmmaG8AAAAASUVORK5CYII.png")
    return embed


# tuki loh še dubiš učilnco
# predure


# def urnik_by_test(selected_razred):
#     urnik_url = "https://www.easistent.com/urniki/307dd36f0b3533186a238aa0411889e402ec7478/razredi/423682"
#     #urnik_url = "https://www.easistent.com/urniki/12296fadef0fe622b9f04637b58002abc872259c/razredi/421675"
#     uClient = uRec(urnik_url)
#     page_html = uClient.read()
#     uClient.close()
#     page_soup = soup(page_html, "html.parser")

#     try:
#         razred_value = page_soup.find_all(
#             "option", string=selected_razred)[0]["value"]
#     except IndexError:
#         try:
#             selected_razred = selected_razred.split(".")
#             selected_razred = str(
#                 selected_razred[0]) + ". " + str(selected_razred[1])
#             razred_value = page_soup.find_all(
#                 "option", string=selected_razred)[0]["value"]
#         except IndexError:
#             selected_razred = selected_razred.lower()
#             selected_razred = selected_razred.split(".")
#             selected_razred = str(
#                 selected_razred[0]) + "." + str(selected_razred[1])
#             razred_value = page_soup.find_all(
#                 "option", string=selected_razred)[0]["value"]

#     urnik_url = f"https://www.easistent.com/urniki/307dd36f0b3533186a238aa0411889e402ec7478/razredi/{razred_value}"
#     uClient = uRec(urnik_url)
#     page_html = uClient.read()
#     uClient.close()
#     page_soup = soup(page_html, "html.parser")

#     linja = page_soup.find_all(["tr", "tr"])
#     # linja = page_soup.find_all("td", {"class": "ednevnik-seznam_ur_teden-td"})

#     for ura in linja:
#         hour = linja[2].find_all(
#             "td", {})
#         print(hour[0])
#     # print(linja)


# urnik_by_test("1.B")
