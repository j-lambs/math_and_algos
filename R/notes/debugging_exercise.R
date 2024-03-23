is_prime <- function(x) {
  if (x == 2) {
    return(TRUE)
  } else if (any(x %% 2:(x-1) == 0)) {
    return(FALSE)
  } else {
    return(TRUE)
  }
}
is_palindrome <- function(x) {
  x_char <- as.character(x)
  x_char <- stringr::str_split(x_char, "")[[1]]
  x_rev <- rev(x_char)
  return(x_char == x_rev)
}
for (i in 1:1000) {
  if (is_prime(i) & is_palindrome(i)) {
    print(i)
  }
}
