
view_count_all <- cbind(view_count_1, view_count_2)
view_count_loud <- view_count_all[,c("Rachel", "Walter", "Dave")]
total_views_loud <- colSums(view_count_loud)


commission_rate <- star_wars_matrix * commission
 remaining <- star_wars_matrix - commission_rate
remaining_tot <- rowSums(remaining)
profit <- remaining_tot - budget
