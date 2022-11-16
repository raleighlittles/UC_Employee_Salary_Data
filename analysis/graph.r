library(ggplot2)
library(ggstatsplot)

all_uni_2021_data <- read.csv(file = "/home/raleigh/github/UC_Employee_Salary_Data/data/parsed/UCOP_Data_2021.csv", stringsAsFactors = TRUE)

ggbetweenstats(data=all_uni_2021_data, x=location, y=gross.pay, outlier.tagging = TRUE, outlier.label = title, pairwise.comparisons = FALSE, title = "2021 Salary by UC campus", results.subtitle = FALSE, k = 0)

ggsave("2021_data.svg", plot = last_plot(), device = "svg", dpi = "retina")
