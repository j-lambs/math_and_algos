library(tidyverse)
print("hello world")
data()
View(mpg) # open new tab to see dataframe
?mpg      # get documentation
# glimpse(mpg)  # show little preview of dataframe in console


# introduction to filtering data
good_mpg_cars <- filter(mpg, cty >= 25) 
hwy_nissan <- filter(mpg, manufacturer == "nissan")
view(hwy_nissan)

# mutating / changing data
metric <- mutate(mpg, cty_metric = 0.425144 * cty)
view(metric)

# pipes
metric <- mpg %>% 
  mutate(mpg, cty_metric = 0.425144 * cty) # same thing as above, just using pipes

# group_by
mpg %>% 
  group_by(class) %>% 
  summarise(mean(cty),
            median(cty))

# ggplot2
ggplot(mpg, aes(x = cty))

library(ggplot2)
mpg_plot <- ggplot(mpg, aes(x = displ, y = hwy)) + 
  geom_point(aes(color = class))
mpg_plot
