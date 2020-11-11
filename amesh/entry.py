from io import BytesIO
from urllib.parse import urljoin
from datetime import datetime, timedelta

import pytz
import requests
from PIL import Image


class Entry():

    amesh_url = "http://tokyo-ame.jwa.or.jp"
    map_000 = "/map/map000.jpg"
    msk_000 = "/map/msk000.png"
    __mesh_format = "/mesh/000/%Y%m%d%H%M.gif"
    __offset_minutes = 5

    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.rounded = self.__get_rounded_time(timestamp)
        self.mesh_url = urljoin(
            self.amesh_url, self.rounded.strftime(self.__mesh_format))

    def __get_rounded_time(self, t: datetime) -> datetime:
        rounded = t - timedelta(minutes=self.__offset_minutes)
        return rounded.replace(minute=(rounded.minute - (rounded.minute % self.__offset_minutes)))

    def to_image(self) -> Image:
        img_map = self.__get_image_for(urljoin(self.amesh_url, self.map_000)).convert("RGBA")
        img_msk = self.__get_image_for(urljoin(self.amesh_url, self.msk_000)).convert("RGBA")
        img_mesh = self.__get_image_for(self.mesh_url).convert("RGBA")
        img_map.paste(img_mesh, (0, 0), img_mesh)
        img_map.paste(img_msk, (0, 0), img_msk)
        return img_map

    def to_bytes(self) -> bytes:
        img = self.to_image()
        buf = BytesIO()
        img.save(buf, format='PNG')
        return buf.getvalue()

    def __get_image_for(self, img_url: str) -> Image:
        response = requests.get(img_url)
        return Image.open(BytesIO(response.content))


def get_entry(now: datetime = None) -> Entry:
    now = now if now is not None else datetime.now(
        tz=pytz.timezone("Asia/Tokyo"))
    entry = Entry(now)
    return entry
