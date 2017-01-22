# Gospel - glimpse into your financial future

## Inspiration
CPF is a uniquely Singaporean construct that takes out a huge chunk of our spending power. It is a form of forced savings that sadly, few Singaporeans truly understand. We decided we wanted to better understand CPF and its quirks, and this came in the form of creating a visualization of our financial futures. And that's how Gospel came about.

## What it does
Based on some basic information like age, salary, and monthly expenditure, Gospel makes an educated guess at how your wealth will grow over your lifetime. 

## How we built it
We started with a simple Google Spreadsheet to create the MVP. It worked so well we decided to use the Google Sheets API to perform the backend logic for our app. The app is served using Flask, and the front-end was built using Highcharts.js (charting library) and Bootstrap. 

## Challenges we ran into
- Google Sheets API wasn't as easy to use as expected
- Google Sheets not as performant as expected
- CPF wasn't as straightforward as we expected
- Network was slow at times 

## Accomplishments that we're proud of
We managed to successfully integrate the Google Sheets API and built a decent-looking product. 

## What we learned
A lot about CPF. And a bit of Excel formulas. And how to deal with json and charting libraries.

## What's next for Gospel
Our original vision for Gospel was fully interactive visualization that updated dynamically with different form inputs. Google Sheets isn't fast enough for that, so we hope to move the backend logic to client-side to allow for faster visualizations. This will also allow for us to support more users.



 
