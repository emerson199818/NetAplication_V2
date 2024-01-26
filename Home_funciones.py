import tkinter as tk
from  tkinter import ttk
import pandas as pd
import time

import Variables

def Centro_principal(frame):
	global Centro_p
	Centro_p = tk.Frame(frame, bg="blue")
	Centro_p.pack(side="top", fill="both", expand=True)

	
	return frame