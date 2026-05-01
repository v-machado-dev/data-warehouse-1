-- import

with source as (
    select
        "Date",
        "Close",
        "symbol"
    from {{ source ('postgres', 'commodities') }}
),

-- renamed

renamed as (
    select
        cast("Date" as Date) as data,
        "Close" as closing_price,
        symbol
    from
        source
)

select * from renamed
