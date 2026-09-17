#Generator
def generator():
    yield 1
    yield 2
    yield 3
r=generator()
print(next(r))
print(next(r))
print(next(r))
#print(next(r)) # Error due to yields statements completed