# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:29:04 2021

@author: K Raghavendiran
"""

import altair as alt
import pandas as pd
from week6_codefile import Table

source = pd.DataFrame(Table)


alt.Chart(source).mark_bar().encode(
  x='start',
  x2='end',
  y='mc',
  color=alt.Color('job:N'),).properties(width=700,height=200)