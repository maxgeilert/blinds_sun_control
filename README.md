[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

# HACS python script for sun-based blinds control
A python script that can open and close cover entities in home assistant based on the sun.

# Prequisits
- enable sun azimuth- and elevation-entities in the default sun-integration
- add the following template sensor to your configuration
~~~
      sun_direction:
        friendly_name: "Sun direction"
        value_template: >-
          {% if states("sensor.sun_solar_azimuth") | int > 12.5 and states("sensor.sun_solar_azimuth") | int < 57.5 %}
          N/E
          {% elif states("sensor.sun_solar_azimuth") | int > 57.6 and states("sensor.sun_solar_azimuth") | int < 102.5 %}
          E
          {% elif states("sensor.sun_solar_azimuth") | int > 102.6 and states("sensor.sun_solar_azimuth") | int < 147.5 %}
          S/E
          {% elif states("sensor.sun_solar_azimuth") | int > 147.6 and states("sensor.sun_solar_azimuth") | int < 192.5 %}
          S
          {% elif states("sensor.sun_solar_azimuth") | int > 192.6 and states("sensor.sun_solar_azimuth") | int < 237.5 %}
          S/W
          {% elif states("sensor.sun_solar_azimuth") | int > 237.6 and states("sensor.sun_solar_azimuth") | int < 282.5 %}
          W
          {% elif states("sensor.sun_solar_azimuth") | int > 282.6 and states("sensor.sun_solar_azimuth") | int < 327.5 %}
          N/W
          {% else %}
          N
          {% endif %}
~~~

# Example automation
~~~
- alias: Blinds Control
  description: 'sun based control for blinds'
  trigger:
  - platform: state
    entity_id: sensor.sun_direction
    id: changed
  condition:
    - condition: numeric_state
      entity_id: weather.forecast_home
      attribute: temperature
      above: 25
  action:
  - service: python_script.blinds_sun_control
    data:
      blinds:
        - entity: cover.balcony_door
          direction: "W"
        - entity: cover.livingroom
          direction: "W"
        - entity: cover.office
          direction: "W"
        - entity: cover.bathroom
          direction: "N"
        - entity: cover.storage
          direction: "N"
        - entity: cover.bedroom
          direction: "S"
      control_entity: sensor.sun_direction
  mode: single
  id: blindscontrol
~~~
# Versions
### 0.0.1
Initial Release