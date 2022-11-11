from ldap3 import Server, Connection, SUBTREE

from config import settings


def get_info_ad_from_settings(name):
    """Получение параметров из файла settings.py"""
    return getattr(settings, name)


def GetDataFromAD(user_login):
    """Получение данных пользователя из Active Directory на основе предоставленного логина"""
    AD_SERVER = get_info_ad_from_settings('AD_SERV')
    AD_USER = get_info_ad_from_settings('AD_US')
    AD_PASSWORD = get_info_ad_from_settings('AD_PASS')
    AD_SEARCH_TREE = get_info_ad_from_settings('AD_SEARCH')
    server = Server(AD_SERVER)
    conn = Connection(server, user=AD_USER, password=AD_PASSWORD)
    conn.bind()
    conn.search(AD_SEARCH_TREE, '(sAMAccountName='+user_login+')', SUBTREE, attributes=['DisplayName', 'department', 'title', 'telephoneNumber'])
    user = conn.entries
    return [user[0].displayName, user[0].telephoneNumber, user[0].department, user[0].title]