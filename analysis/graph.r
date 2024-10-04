library(ggplot2)
library(ggstatsplot)

all_uni_2023_data <- read.csv(file = "../data/UCOP_Data_2023.csv", stringsAsFactors = TRUE)

ggbetweenstats(data=all_uni_2023_data, x=location, y=gross.pay, outlier.tagging = TRUE, outlier.label = title, pairwise.comparisons = FALSE, title = "2023 Salary by UC campus", results.subtitle = FALSE, k = 0)

ggsave("2023_data.svg", plot = last_plot(), device = "svg", dpi = "retina")

