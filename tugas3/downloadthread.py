import logging
import threading
import requests
import os



def download_gambar(url=None):
    if (url is None):
        return False
    namafile = os.path.basename(url)
    logging.warning(f"writing image {namafile}")
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpeg'

    content_type = ff.headers['Content-Type']
    if (content_type in list(tipe.keys())):

        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()
        logging.warning(f"writing {namafile} success")
    else:
        return False

if __name__=='__main__':
    gambar=['https://effigis.com/wp-content/uploads/2015/02/Airbus_Pleiades_50cm_8bit_RGB_Yogyakarta.jpg', #Yang ini agak lama downloadnya karena 40Mb lebih
            'https://vignette.wikia.nocookie.net/cookierun/images/1/19/Cherry_Blossom_Cookie.png',
            'https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg',
            'https://pbs.twimg.com/media/ERvqjzgU0AAMeUc.jpg']
    threads = []
    for i in range(4):
        t = threading.Thread(target=download_gambar, args=(gambar[i],))
        threads.append(t)

    for thr in threads:
        thr.start()
    # download_gambar('https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg')