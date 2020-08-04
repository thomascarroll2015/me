TODO: Reflect on what you learned this week and what is still unclear.

Using describe() on categorical data will produce similar output to a Series or DataFrame of type string.

Categorical data has a categories and a ordered property, which list their possible values and whether the ordering matters or not. These properties are exposed as s.cat.categories and s.cat.ordered. If you don’t manually specify categories and ordering, they are inferred from the passed arguments.