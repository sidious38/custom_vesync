"""Constants for VeSync Component."""

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import UnitOfTemperature, UnitOfTime

DOMAIN = "vesync"
VS_DISCOVERY = "vesync_discovery_{}"
SERVICE_UPDATE_DEVS = "update_devices"

VS_BUTTON = "button"
VS_SWITCHES = "switches"
VS_FAN = "fan"
VS_FANS = "fans"
VS_LIGHTS = "lights"
VS_SENSORS = "sensors"
VS_HUMIDIFIERS = "humidifiers"
VS_NUMBERS = "numbers"
VS_BINARY_SENSORS = "binary_sensors"
VS_MANAGER = "manager"

VS_LEVELS = "levels"
VS_MODES = "modes"

VS_MODE_AUTO = "auto"
VS_MODE_HUMIDITY = "humidity"
VS_MODE_MANUAL = "manual"
VS_MODE_SLEEP = "sleep"
VS_MODE_TURBO = "turbo"

VS_TO_HA_ATTRIBUTES = {"humidity": "current_humidity"}

VS_FAN_TYPES = ["VeSyncAirBypass", "VeSyncAir131", "VeSyncAirBaseV2"]
VS_HUMIDIFIERS_TYPES = ["VeSyncHumid200300S", "VeSyncHumid200S", "VeSyncHumid1000S"]
VS_AIRFRYER_TYPES = ["VeSyncAirFryer158"]


DEV_TYPE_TO_HA = {
    "ESL100": "bulb-dimmable",
    "ESL100CW": "bulb-tunable-white",
    "ESO15-TB": "outlet",
    "ESW03-USA": "outlet",
    "ESW01-EU": "outlet",
    "ESW15-USA": "outlet",
    "wifi-switch-1.3": "outlet",
    "WHOGPLUG": "outlet",
    "ESWL01": "switch",
    "ESWL03": "switch",
    "ESD16": "walldimmer",
    "ESWD16": "walldimmer",
}


BINARY_SENSOR_TYPES_AIRFRYER = {
    # unique_id,name # icon, #attribute read,
    "is_heating": [
        "is_heating",
        "preheating",
        "mdi:pot-steam-outline",
    ],
    "is_cooking": [
        "is_cooking",
        "cooking",
        "mdi:rice",
    ],
    "is_running": [
        "is_running",
        "running",
        "mdi:pause",
    ],
}


SENSOR_TYPES_AIRFRYER = {
    # unique_id ,#name ,# unit of measurement,# icon, # device class, #attribute read,
    "current_temp": [
        "current_temperature",
        "Current temperature",
        UnitOfTemperature.CELSIUS,
        None,
        SensorDeviceClass.TEMPERATURE,
        "current_temp",
    ],
    "cook_set_temp": [
        "set_temperature",
        "Set temperature",
        UnitOfTemperature.CELSIUS,
        None,
        SensorDeviceClass.TEMPERATURE,
        "cook_set_temp",
    ],
    "cook_last_time": [
        "cook_last_time",
        "Cook Remaining",
        UnitOfTime.MINUTES,
        "mdi:timer",
        UnitOfTime.MINUTES,
        "cook_last_time",
    ],
    "preheat_last_time": [
        "preheat_last_time",
        "Preheat Remaining",
        UnitOfTime.MINUTES,
        "mdi:timer",
        UnitOfTime.MINUTES,
        "preheat_last_time",
    ],
    "cook_status": [
        "cook_status",
        "Cook Status",
        None,
        "mdi:rotate-3d-variant",
        None,
        "cook_status",
    ],
    # "remaining_time": [
    #    "remaining_time",
    #    "running:",
    #    UnitOfTime.MINUTES,
    #    "mdi:timer",
    #    UnitOfTime.MINUTES,
    #    "remaining_time",
    # ],
}
