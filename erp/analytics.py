# analytics.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from file_handler import students, courses


def credit_analysis():
    if not courses:
        print("No courses")
        return

    credits = np.array([c.credits for c in courses])

    print("Average:", np.mean(credits))
    print("Max:", np.max(credits))
    print("Min:", np.min(credits))


def department_visualization():
    dept_list = [s.department for s in students]

    if not dept_list:
        print("No data")
        return

    df = pd.DataFrame(dept_list, columns=["Department"])
    counts = df["Department"].value_counts()

    print("\nDepartment Count:\n", counts)

    counts.plot(kind='bar')
    plt.title("Department Distribution")
    plt.xlabel("Department")
    plt.ylabel("Students")
    plt.show()