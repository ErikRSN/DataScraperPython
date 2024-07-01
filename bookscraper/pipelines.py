class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Strip all whitespaces from strings
        field_names = adapter.fields.keys()
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                if isinstance(value, list) and len(value) > 0:
                    adapter[field_name] = value[0].strip()

        # Category & Product Type --> switch to lowercase
        lowercase_keys = ['category', 'product_type']
        for key in lowercase_keys:
            value = adapter.get(key)
            if value:
                adapter[key] = value.lower()

        # Price --> convert to float
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            if value:
                value = value.replace('£', '')
                try:
                    adapter[price_key] = float(value)
                except ValueError:
                    adapter[price_key] = 0.0

        # Availability --> extract number of books in stock
        availability_string = adapter.get('availability')
        if availability_string:
            split_string_array = availability_string.split('(')
            if len(split_string_array) >= 2:
                availability_array = split_string_array[1].split(' ')
                try:
                    adapter['availability'] = int(availability_array[0])
                except ValueError:
                    adapter['availability'] = 0
            else:
                adapter['availability'] = 0

        # Reviews --> convert string to number
        num_reviews_string = adapter.get('num_reviews')
        try:
            adapter['num_reviews'] = int(num_reviews_string)
        except ValueError:
            adapter['num_reviews'] = 0

        # Stars --> convert string to number
        stars_string = adapter.get('stars')
        if stars_string:
            split_string_array = stars_string.split(' ')
            stars_text_value = split_string_array[1].lower()
            stars_mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
            adapter['stars'] = stars_mapping.get(stars_text_value, 0)

        return item