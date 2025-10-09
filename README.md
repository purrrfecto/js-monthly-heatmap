
## Live Demo
https://purrrfecto.github.io/js-monthly-heatmap/

### hella thanks chatgpt!

- javascript to create monthly heatmap to visualize how many events occurance in each day
- also runs as local html file
- used to see what day is more busy and what day is not


### ✨ Features Recap

| Feature                    | Description                                    |
| -------------------------- | ---------------------------------------------- |
| ✅ **Google Sheets Paste**  | Accepts tab-separated or comma-separated input |
| ✅ **Multi-Month Grouping** | Each month displayed separately                |
| ✅ **Weekday Alignment**    | Days start on correct weekday                  |
| ✅ **YlGn Gradient**        | Yellow → Green color scale                     |
| ✅ **Legend**               | Dynamic, scaled to max count                   |
| ✅ **Interactive Tooltip**  | Hover or tap a day to see exact date + count   |

---

### 🧩 Example Input (directly paste from Sheets)

| date       | count |
| ---------- | ----- |
| 2023-12-06 | 1     |
| 2023-12-14 | 2     |
| 2024-01-01 | 3     |
| 2024-01-05 | 1     |

Just copy those cells → paste into the textbox → click **Render Heatmaps** ✅

---

### Extra
- Export and save the calendar as .ics file 
- in ```icsEventCount.py```, point ```ics_file_path``` to the downloaded .ics file
- ```python3 -m icsEventCount.py```
- terminal should output the date and counts
