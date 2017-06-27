"""
Fibonacci with for loops

function getFib(position) {
  if (position == 0) { return 0; }
  if (position == 1) { return 1; }
  var first = 0,
      second = 1,
      next = first + second;
  for (var i = 2; i < position; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
}

"""

def fibonacci(position):
  if position == 0
    return 0
  elif position == 1:
    return 1
  
  first = 0
  second = 1
  _next = first + second

  for i in range(position):
    first = second
    second = next
    _next = first + second
  return _next