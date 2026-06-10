from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Insertion Sort
def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Merge Sort
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


@app.route("/", methods=["GET", "POST"])
def index():

    bubble_time = None
    insertion_time = None
    merge_time = None

    winner = None
    complexity = None
    sorted_fares = None

    if request.method == "POST":

        fares = request.form["fares"]

        arr = list(map(int, fares.split(",")))

        start = time.perf_counter()
        bubble_sort(arr.copy())
        bubble_time = round(
            (time.perf_counter() - start) * 1000,
            6
        )

        start = time.perf_counter()
        insertion_sort(arr.copy())
        insertion_time = round(
            (time.perf_counter() - start) * 1000,
            6
        )

        start = time.perf_counter()
        sorted_fares = merge_sort(arr.copy())
        merge_time = round(
            (time.perf_counter() - start) * 1000,
            6
        )

        times = {
            "Bubble Sort": bubble_time,
            "Insertion Sort": insertion_time,
            "Merge Sort": merge_time
        }

        winner = min(times, key=times.get)

        if winner == "Merge Sort":
            complexity = "O(n log n)"
        else:
            complexity = "O(n²)"

    return render_template(
        "index.html",
        bubble_time=bubble_time,
        insertion_time=insertion_time,
        merge_time=merge_time,
        winner=winner,
        complexity=complexity,
        sorted_fares=sorted_fares
    )


if __name__ == "__main__":
    app.run(debug=True)