#!/usr/bin/env python3
import pytest

from ..main import parse, extract


def test_vk_user_profile_full():
    info = extract(parse('https://vk.com/idsvyatoslavs')[0])

    assert info.get('uid') == '134173165'
    assert info.get('username') == 'idsvyatoslavs'
    assert info.get('name') in ('Святослав Степанов', 'Svyatoslav Stepanov')

def test_vk_user_profile_no_username():
    info = extract(parse('https://vk.com/id568161939')[0])

    assert info.get('uid') == '568161939'
    assert info.get('username') == None
    assert info.get('name') in ('Юля Заболотная', 'Yulya Zabolotnaya')

def test_yandex_disk():
    info = extract(parse('https://yadi.sk/d/KDk-D4vhGFbhb')[0])

    assert info.get('yandex_uid') == '106917461'
    assert info.get('name') == 'samografova.viktoria'

@pytest.mark.skip(reason="failed from github CI infra IPs")
def test_instagram():
    info = extract(parse('http://192.168.64.22:3000/')[0])

    assert info.get('uid') == '21965519'
    assert info.get('username') == 'xenia_sobchak'

def test_medium():
    info = extract(parse('https://medium.com/@lys1n')[0])

    assert info.get('uid') == '4894fec6b289'
    assert info.get('username') == 'lys1n'
    assert info.get('twitter_username') == 'lys1n'
    assert info.get('name') == 'Марк Лясин'

def test_ok():
    info = extract(parse('https://ok.ru/profile/46054003')[0])

    assert info.get('uid') == '46054003'

    info = extract(parse('https://ok.ru/andrey.ostashenya')[0])

    assert info.get('username') == 'andrey.ostashenya'
    assert info.get('uid') == '576861363171'

def test_habr():
    info = extract(parse('https://habr.com/ru/users/m1rko/')[0])

    assert info.get('uid') == '1371978'
    assert info.get('username') == 'm1rko'

@pytest.mark.skip(reason="broken, https://github.com/soxoj/socid_extractor/issues/3")
def test_twitter():
    info = extract(parse('https://twitter.com/esquireru')[0])

    assert info.get('uid') == '163060799'
    assert info.get('username') == 'Esquire Russia'
    assert info.get('name') == 'esquireru'

def test_reddit():
    info = extract(parse('https://www.reddit.com/user/postvolta/')[0])

    assert info.get('uid') == 't2_dexuehm'
    assert info.get('username') == 'postvolta'

def test_facebook_user_profile():
    info = extract(parse('https://ru-ru.facebook.com/anatolijsharij/')[0])

    assert info.get('uid') == '1486042157'
    assert info.get('username') == 'anatolijsharij'

def test_facebook_group():
    info = extract(parse('https://www.facebook.com/discordapp/')[0])

    assert info.get('uid') == '858412104226521'
    assert info.get('username') == 'discord'

def test_github():
    info = extract(parse('https://github.com/soxoj')[0])

    assert info.get('uid') == '31013580'
    assert info.get('username') == 'soxoj'

def test_yandex_disk_photos():
    info = extract(parse('https://yadi.sk/a/oiySK_wg3Vv5p4')[0])

    assert info.get('yandex_uid') == '38569641'
    assert info.get('name') == 'Вербочка'

def test_my_mail_main():
    info = extract(parse('https://my.mail.ru/mail/zubovo/')[0])

    assert info.get('uid') == '13425818'
    assert info.get('name') == 'Олег Зубов'
    assert info.get('username') == 'zubovo'
    # there is no auId
    assert info.get('email') == 'zubovo@mail.ru'
    assert info.get('isVip') == 'False'
    assert info.get('isCommunity') == 'False'
    assert info.get('isVideoChannel') == 'False'

def test_my_mail_communities():
    # also video, apps, photo
    info = extract(parse('https://my.mail.ru/mail/zubovo/communities/')[0])

    assert info.get('uid') == '13425818'
    assert info.get('name') == 'Олег Зубов'
    assert info.get('username') == 'zubovo'
    assert info.get('auId') == '6667000454247668890'
    assert info.get('email') == 'zubovo@mail.ru'
    assert info.get('isVip') == 'False'
    assert info.get('isCommunity') == 'False'
    assert info.get('isVideoChannel') == 'False'

@pytest.mark.skip(reason="empty result, additional header needed")
def test_yandex_music_user_profile():
    info = extract(parse('https://music.yandex.ru/handlers/library.jsx?owner=pritisk')[0])

    assert info.get('yandex_uid') == '16480689'
    assert info.get('username') == 'pritisk'
    assert info.get('name') == 'Юрий Притиск'

def test_yandex_znatoki_user_profile():
    info = extract(parse('https://yandex.ru/znatoki/user/e3795016-b18e-58ba-9112-21c301e53f37/')[0])

    assert info.get('uid') == 'e3795016-b18e-58ba-9112-21c301e53f37'
    assert info.get('yandex_uid') == '980797984'
    assert info.get('name') == 'Настя Рогозинская'

def test_behance():
    info = extract(parse('https://www.behance.net/Skyratov', 'ilo0=1')[0])

    assert info.get('uid') == '39065909'
    assert info.get('username') == 'Skyratov'
    assert info.get('last_name') == 'Skuratov'
    assert info.get('first_name') == 'Vasiliy'

def test_500px():
    info = extract(parse('https://500px.com/the-maksimov')[0])

    assert info.get('uid') == '23896'
    assert info.get('username') == 'The-Maksimov'
    assert info.get('name') == 'Maxim Maximov'
    assert info.get('qq_uid') == None
    assert info.get('fb_uid') == None
    assert info.get('instagram_username') == 'the.maksimov'
    assert info.get('twitter_username') == 'The_Maksimov'
    assert info.get('website') == 'vk.com/id156603747'
    assert info.get('facebook_page') == 'facebook.com/the.maksimov'
    assert info.get('facebook_uid') == '100001789363632'

def test_google_documents_cookies():
    cookies = open('google.test.cookies').read()
    info = extract(parse('https://docs.google.com/spreadsheets/d/1HtZKMLRXNsZ0HjtBmo0Gi03nUPiJIA4CC4jTYbCAnXw/edit#gid=0', cookies)[0])

    assert info.get('org_domain') == 'breakoutcommerce.com'
    assert info.get('org_name') == 'Gooten'

def test_bitbucket():
    info = extract(parse('https://bitbucket.org/arny/')[0])

    assert info.get('uid') == '57ad342a-ec8f-42cb-af05-98175b72b8db'
    assert info.get('username') == 'arny'
    assert info.get('created_at') == '2009-11-23T10:41:04.355755+00:00'

def test_steam():
    info = extract(parse('https://steamcommunity.com/id/GabrielSantosMariano/')[0])

    assert info.get('uid') == '76561198315585536'
    assert info.get('username') == 'GabrielSantosMariano'
    assert info.get('name') == 'Gabriel! Santos, Mariano.'

def test_steam_hidden():
    info = extract(parse('https://steamcommunity.com/id/Elvoc/')[0])

    assert info.get('uid') == '76561197976127725'
    assert info.get('username') == 'Elvoc'
    assert info.get('name') == 'Elvoc'

def test_yandex_realty_offer_cookies():
    cookies = open('yandex.test.cookies').read()
    info = extract(parse('https://realty.yandex.ru/offer/363951114410351104/', cookies)[0])

    assert info.get('uid') == '86903473'
    assert info.get('name') == 'Севостьянова Мария Владимировна'

def test_gitlab_cookies():
    cookies = open('gitlab.test.cookies').read()
    info = extract(parse('https://gitlab.com/markglenfletcher', cookies)[0])

    assert info.get('uid') == '419655'

def test_blogger():
    info = extract(parse('https://b0ltay.blogspot.ru')[0])

    assert info.get('uid') == '10725121405978587846'
    assert info.get('blog_id') == '9057808199412143402'

def test_d3():
    info = extract(parse('https://d3.ru/user/deer00hunter')[0])

    assert info.get('uid') == '75504'

def test_stack_exchange():
    info = extract(parse('https://stackoverflow.com/users/758202/zzart')[0])

    assert info.get('uid') == '758202'
    assert info.get('stack_exchange_uid') == '395311'

def test_soundcloud():
    info = extract(parse('https://soundcloud.com/danielpatterson')[0])

    assert info.get('uid') == '78365'
    assert info.get('username') == 'danielpatterson'
    assert info.get('name') == 'Daniel Patterson'

def test_vcru():
    info = extract(parse('https://vc.ru/u/6587-pavel-stolyarov')[0])

    assert info.get('uid') == '6587'
    assert info.get('username') == '6587-pavel-stolyarov'
    assert info.get('name') == 'Павел Столяров'

def test_livejournal():
    info = extract(parse('https://julia-klay.livejournal.com/')[0])

    assert info.get('uid') == '83505610'
    assert info.get('name') == 'julia_klay'
    assert info.get('username') == 'julia_klay'
    assert info.get('is_personal') == 'True'
    assert info.get('is_community') == 'False'

@pytest.mark.skip(reason="doesnt work without proxy, 503 error")
def test_myspace():
    info = extract(parse('https://myspace.com/katelynryry')[0])

    assert info.get('uid') == '8158005'
    assert info.get('username') == 'katelynryry'

def test_youtube():
    info = extract(parse('https://www.youtube.com/channel/UCbeOQiPo5SjX8Q_IoSooBig')[0])

    assert info.get('gaia_id') == '117503292148966883754'
    assert info.get('name') == 'Art NI'

def test_google_maps():
    info = extract(parse('https://www.google.com/maps/contrib/117503292148966883754')[0])

    assert info.get('contribution_level') == 'Level 3 Local Guide | 113 Points'
    assert info.get('name') == 'Art NI'

def test_deviantart():
    info = extract(parse('https://www.deviantart.com/muse1908')[0])

    assert info.get('country') == 'France'
    assert int(info.get('registered_for_seconds')) > 476254777
    assert info.get('gender') == 'female'
    assert info.get('website') == 'www.patreon.com/musemercier'
    assert info.get('username') == 'Muse1908'
    assert info.get('links') == "['https://www.facebook.com/musemercier', 'https://www.instagram.com/muse.mercier/', 'https://www.patreon.com/musemercier']"
    assert info.get('tagline') == 'Nothing worth having is easy...'

def test_vimeo():
    info = extract(parse('https://vimeo.com/alexaimephotography')[0])

    assert info.get('uid') == '75857717'
    assert info.get('name') == 'AlexAimePhotography'
    assert info.get('username') == 'alexaimephotography'
    assert info.get('location') == 'France'
    assert info.get('created_at') == '2017-12-06 06:49:28'
    assert info.get('is_staff') == 'False'
    assert info.get('links') == "['https://500px.com/alexaimephotography', 'https://www.flickr.com/photos/photoambiance/', 'https://www.instagram.com/alexaimephotography/', 'https://www.youtube.com/channel/UC4NiYV3Yqih2WHcwKg4uPuQ', 'https://flii.by/alexaimephotography/']"
