import googleapiclient.discovery
import re

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

def duration(v_id):

    api_key = 'AIzaSyAThwinMHqAPzectaIrV7-RdL8wkrpfLa0'

    service = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # v_id = ['QXeEoD0pB3E', 'hEgO047GxaQ', 'mbryl4MZJms', 'DWgzHbglNIo', 'TqPzwenhMj0', 'Eaz5e6M8tL4', 'Mf7eFtbVxFM', '2IsF7DEtVjg', '4V14G5_CNGg', '1U8TI16AR4s', '_OZIAHg5i7M', 'gCCVsvgR2KU', 'v5MR5JnKcZI', 'AWAjbtWBzGs', '3dpJrMtxYeo', 'Bwd9hr5Fz5E', 'UAMMEmga0WI', 'PyfKCvHALj8', 'EkYrfV7M1ks', 'akcEaEH91gI', '4OX49nLNPEE', 'PqFKRqpHrjw', 'HZARImviDxg', '0ZvaDa8eT5s', 'yCZBnjF4_tU', 'JCRpVwtVL4I', 'k8SXsT5TLxQ', '38svC3U7hVo', 'SpTAxH_Geow', '6a39OjkCN5I', '9c9qhIcB3NA', '8LlXhtfNZEQ', 'NYPKbmE0H6E', '8sF85TyunQA', 'Blzp9iuhZqo', 'BVfCWuca9nw', 'ijXMGpoMkhQ', 'eci9iU_s6Ag', 'kB829ciAXo4', 'QYUbLevwgDQ', 'fsAzeNZXvkE', '7Sv4NmvdHcw', 'gfhtaP5Wq7M', 'XkL3SUioNvo', 'TqqQld6m6A0', 'hYzwCsKGRrg', 'kj850Y8y8FI', 'yNzxXZfkLUA', '1RuMJ53CKds', 'pzNISmtmzcY', '7hjgRn-vfVQ']

    # 'gZwPdqC2Os0', '8O5kX73OkIY', 'WIP3-woodlU', 'ic6wdPxcHc0', 'RSQjxL5WRNM', 'lVfGQOzzRCM', 'b7JzgybKvys', 'Cn7AkDb4pIU', '6P-P879BcHQ', 'P1vH3Pfw6BI', 'CuK0g8OFzwo', '9wd50TKv_OQ', 'CcTzTuIsoFk', 'UDmJGvM-OUw', 'Dyu08G2l71c', 'mziIj4M_uwk', '6SPDvPK38tw', 'GqHLztqy0PU', 'aequTxAvQq4', 'ECxZtt6n90E', '0BhSWyDEDC4', 'UldZOLylez4', 'DE-ye0t0oxE', 'Vca808JTbI8', '5KjapFQNxUo', 'WDEyt2VHpj4', 'vR5utJvN4JY', 'UBLONzkmReE', 'udO6gSLXujU', 'qj-V2Ep4coY', 'u4kr7EFxAKk', 'kU_ZtZhmmEU', '5NU6w5VhmMc', '6-F7nP1DwJs', 'SIyxjRJ8VNY', 'VuETrwKYLTM', 'ykpuyNy5oUM', '4UMs7DxWn_Q', 'GNlIe5zvBeQ', 'Kz-G6GnumsI', '_xBMAoDfydg', 'QD4GlXtf-WU', 'GGkFg52Ot5o', 'K8Uem148uOU', 'Tt3mgy2ECug', 'Huk9tIRD_rQ', 'cHBn87eRFwo', 'nuW0o4-dSpo', '7E1M1W9o7PA', 'd--mEqEUybA', '69YkZqZgz9s', 'sU7_reASCAw', 'iLhcV7t3zug', 'ExTaxRmDnP8', '6Q5OVCKufBU', 'JXBCw_4gwc0', 'Mf_97YaUKag', 'teaeVbcT9BI', 'iT15mk4y1iw', 'YfO28Ihehbk', 'BsVQ_cBmEwg'

    arr = []

    request = service.videos().list(
        part = 'contentDetails',
        id = ','.join(v_id),
    )
    
    response = request.execute()

    for i in response['items']:
        time = i['contentDetails']['duration']

        hours = hours_pattern.search(time)
        minutes = minutes_pattern.search(time)
        seconds = seconds_pattern.search(time)

        hours = hours.group(1) if hours else 0
        minutes = minutes.group(1) if minutes else 0
        seconds = seconds.group(1) if seconds else 0

        dura = str(hours) + ':' + str(minutes) + ':' + str(seconds)

        arr.append(dura)

    return arr

