from progress.bar import Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar, IncrementalBar, PixelBar, ShadyBar
import time

# Bar
bar = Bar('Bar', max=30)
for i in range(30):
    time.sleep(0.05)
    bar.next()
bar.finish()

# ChargingBar
bar = ChargingBar('Charging', max=30)
for i in range(30):
    time.sleep(0.05)
    bar.next()
bar.finish()

# FillingSquaresBar
bar = FillingSquaresBar('Squares', max=30)
for i in range(30):
    time.sleep(0.05)
    bar.next()
bar.finish()

# FillingCirclesBar
bar = FillingCirclesBar('Circles', max=30)
for i in range(30):
    time.sleep(0.05)
    bar.next()
bar.finish()

# IncrementalBar
bar = IncrementalBar('Incremental', max=30)
for i in range(30):
    time.sleep(0.05)
    bar.next()
bar.finish()

# PixelBar
bar = PixelBar('Pixel', max=30)
for i in range(30):
    time.sleep(0.05)
    bar.next()
bar.finish()

# ShadyBar
bar = ShadyBar('Shady', max=30)
for i in range(30):
    time.sleep(0.05)
    bar.next()
bar.finish()

#pls give me a star!