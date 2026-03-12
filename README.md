# Weather Watch — Documentation

## Overview

**Weather Watch** is a desktop weather application built with Python. It fetches real-time weather data from OpenWeatherMap API and displays it in a clean, icon-rich GUI. The app shows current temperature, weather condition, and key metrics like humidity, wind speed, visibility, and pressure for any city.

---

## Libraries Used

| Library | Purpose |
|---|---|
| `tkinter` | Base windowing system (used implicitly by customtkinter) |
| `customtkinter` | Modern-styled UI widgets (frames, labels, entries, images) |
| `Pillow (PIL)` | Loading and rendering `.png` icon images inside the UI |
| `requests` | Making HTTP GET calls to the weather API |


---

## Project Structure

```
Weather App/
│
├── app_ver1.py        
├── app_ver2.py        
├── app_ver3.py
├── appUI.py               # Stores the structure of GUI for application
├── api_key.txt            # Stores the API endpoint with key (not committed to version control)
│
└── res/
    ├── app_icon.ico
    └── icons/
        ├── sun.png
        ├── cloud.png
        ├── rain.png
        ├── storm.png
        ├── snow.png
        ├── fog.png
        ├── min_temp.png
        ├── max_temp.png
        ├── humidity.png
        ├── visib.png
        ├── wind.png
        ├── barometer.png
        ├── home.png
        └── search.png
```

---

## API Configuration

The app reads the full API URL (including the API key) from `api_key.txt`. The URL must contain the placeholder `City_Name`, which gets replaced at runtime with the user's input.

**`api_key.txt` format:**
```
https://api.openweathermap.org/data/2.5/forecast?q=City_Name&appid=YOUR_KEY&units=metric
```


---

## Core Components

### `getWeather(event=None)`
The main data-fetching function. It:
1. Reads the city name from the input field.
2. Loads the API URL from `api_key.txt` and substitutes `City_Name`.
3. Sends a GET request using `requests` and parses the JSON response.
4. Updates all UI labels with the fetched weather values.
5. Dynamically swaps the weather icon based on the `weather_main` condition string (e.g., `"Rain"`, `"Clear"`).

### `load_icon(path, size)`
A helper that wraps `Image.open()` in a `ctk.CTkImage`, making icons compatible with customtkinter's label widget.

---

## UI Layout

The window is fixed at **360 × 640px** and divided into three visual sections:

### 1. Top Container (`container1`)
Displays the city name, a large weather icon (90×90), current temperature, and a short weather description.

### 2. Grid Container (`gridContainer`)
A 3-row × 2-column grid showing six weather metrics, each with a small icon above the value:

| Row | Left | Right |
|-----|------|-------|
| 0 | Min Temp | Max Temp |
| 1 | Humidity | Visibility |
| 2 | Wind Speed | Pressure |

### 3. Bottom Bar
Contains two icon buttons:
- 🏠 **Home** — Placeholder for refresh functionality (`refresh_weather`)
- 🔍 **Search** — Toggles the city input field into view (`open_search`)

---

## Search Flow

1. User clicks the **search icon** → `open_search()` places the hidden `CTkEntry` on screen and focuses it.
2. User types a city name and presses **Enter** → `submit_city()` is called.
3. `submit_city()` hides the entry field and calls `getWeather()` to fetch and display data.

---

## Weather Icon Mapping

The app maps OpenWeatherMap's `weather.main` condition strings to local icon files:

| Condition | Icon File |
|---|---|
| Clear | `sun.png` |
| Clouds | `cloud.png` |
| Rain / Drizzle | `rain.png` |
| Thunderstorm | `storm.png` |
| Snow | `snow.png` |
| Mist / Haze / Fog | `fog.png` |
| *(default)* | `storm.png` |

---
