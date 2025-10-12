mtcars <- read.csv("mtcars.csv")
cor(x=mtcars$mpg, y=mtcars$wt)

plot(mtcars$wt, mtcars$mpg)
