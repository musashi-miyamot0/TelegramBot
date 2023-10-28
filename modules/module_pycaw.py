import re
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from pycaw.pycaw import IAudioEndpointVolume, AudioUtilities

class VolumeControl:
    """
    Класс для управления громкостью аудио на устройстве.
    """

    def __init__(self):
        """
        Инициализирует объект для управления громкостью аудио.

        Получает доступ к аудиоустройству и сохраняет текущее значение громкости.
        """
        self.CLSCTX = CLSCTX_ALL
        self.all_audio = AudioUtilities.GetSpeakers()
        self.interface = self.all_audio.Activate(IAudioEndpointVolume._iid_, 2, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))

        self.current_volume = self.volume.GetMasterVolumeLevelScalar()

    def minus_and_plus(self, increase=True):
        """
        Изменяет громкость звука.

        :param increase: Увеличивать громкость (True) или уменьшать (False).
        """
        volume = 0.1
        new_volume = self.current_volume + volume if increase else self.current_volume - volume
        self.volume.SetMasterVolumeLevelScalar(max(0.0, min(new_volume, 1.0)), None)

    def maximum_and_minimum(self, value: float):
        """
        Устанавливает максимальное или минимальное значение громкости.

        :param value: Значение громкости в диапазоне от 0.0 до 1.0.
        """
        self.volume.SetMasterVolumeLevelScalar(value, None)

    def mute(self, value: bool):
        """
        Устанавливает состояние звука (вкл/выкл).

        :param value: True, чтобы выключить звук (mute), False, чтобы включить (unmute).
        """
        self.volume.SetMute(value, None)

    def current_volume_message(self):
        """
        Возвращает текущее значение громкости в процентах.

        :return: Текущая громкость в виде строки (например, "75%").
        """
        return f'{round(self.current_volume * 100)}%'
