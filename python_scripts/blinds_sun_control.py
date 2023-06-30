#!/usr/bin/env python3

blinds = data.get("blinds",[])
control_entity = data.get("control_entity")

logger.info("blinds_sun_control.py got triggered")
logger.info("control state: {}".format(hass.states.get(control_entity).state))
logger.info("config: {}".format(blinds))

for i in blinds:
    if i["direction"] == hass.states.get(control_entity).state:
        logger.info("{} is equal to {}, lowering shades..".format(i["direction"], hass.states.get(control_entity).state))
        hass.services.call("cover", "set_cover_position", {"entity_id": i["entity"], "position": i["closed_position"]})
    else:
        logger.info("{} is not equal to {}, rising shades..".format(i["direction"], hass.states.get(control_entity).state))
        hass.services.call("cover", "set_cover_position", {"entity_id": i["entity"], position: i["open_position"]})
