# Merge Sort Visualizer

An interactive web page that shows how **merge sort** works, one step at a time. Every number is a bar, and you can watch each comparison and move as the bars get sorted from shortest to tallest.

**Live demo:** https://daa-lab-manual-merge-sort-visualize-nu.vercel.app

## Features

- Play, Pause, Step and Shuffle controls
- Adjustable number of bars (8 to 100) and speed
- A plain-English line that explains every step as it happens
- The current merge is highlighted, and bars outside it are dimmed
- Live counters for comparisons and moves
- Colors for being compared, placed in order, and final position
- Light and dark mode
- Keyboard shortcuts: `Space` play / pause, `→` step, `R` shuffle
- An "Explain this project" side panel with a simplified version of the code, useful for presenting

## How merge sort works

1. **Split** the list in half again and again, until every piece is a single bar. One bar is already sorted.
2. **Merge** two sorted pieces into one by always taking the smaller of the two front bars.
3. Keep merging bigger and bigger pieces until the whole list is one sorted run.

| | |
|---|---|
| Time complexity | O(n log n) in the best, average and worst case |
| Space complexity | O(n) |
| Stable | Yes |

For 100 bars, merge sort needs only a few hundred comparisons. Bubble sort needs about 5,000 for the same list.

## How it is built

Each step of the algorithm is produced by a JavaScript generator function. The function pauses after every comparison and move using `yield`, so the page can draw that one step, update the counters, and write the explanation. This is what makes Play, Pause and Step possible.

It is a single `index.html` file with no libraries, no build step and no dependencies.

## Run it locally

1. Download or clone this repository.
2. Open `merge-sort-visualizer/index.html` in any modern browser.

That is all. No installation is needed.

## Deploy on Vercel

This project lives in a folder of a larger repository, so Vercel needs to know where it is.

1. In Vercel, click **New Project** and import this repository.
2. Next to **Root Directory**, click **Edit** and choose `merge-sort-visualizer`.
3. Set **Framework Preset** to **Other**.
4. Leave Build Command and Output Directory empty, then click **Deploy**.

Every push to the `main` branch updates the live site automatically.

## Project structure

```
merge-sort-visualizer/
├── index.html   # the whole app: page, styles and logic
└── README.md
```
