/*
---------------------------------------Description--------------------------------------

This is a discount calculator created for a freelance worker who wants to calculate 
his rates given 8 hour days with a discount if the project spans several months. He 
wants to give a discount for every full month worked and any remaining days that don't
equal a full month will be billed at his regular rate.

----------------------------------------------------------------------------------------
*/


///////////////////////////////////   Global Variables   ///////////////////////////////

let dailyRate = parseInt(document.getElementById('hourlyRate'));
let numberOfDays = parseInt(document.getElementById('numDays'));
let discountNumber = parseInt(document.getElementById('discount'));
ansr.innerHTML = 0;

////////////////////////////////////////////////////////////////////////////////////////


/* -------------------------------- Daily rate function --------------------------------
Captures how much you make in an 8 hour day 
*/

function dayRate(dailyRate) {
  return dailyRate * 8
}


/* -------------------------------- Calculation function --------------------------------

You'll see in the next function that it takes in 3 parameters. 
1. The dailyRate (which can be used with the dayRate() function above) 
2. numberOfDays - number of days needed to complete the project
3. discount - the percent discount applied for every month of work. I divided it by 100
   to make it into a percentage automatically. The user can't enter a decimal as the input.
*/ 

function priceWithMonthlyDiscount() {

    // If a discount isn't being applied it can still calculate a regular rate
    // with the below 'if' statement

    if (discountNumber.value <= 0) {
      return ansr.innerHTML = dayRate(dailyRate.value) * Math.floor(numberOfDays.value)
    } else {

      // If there's a dicount and it's above 0 the following code will be read and returned.

      let discountConversion = discountNumber.value / 100;
      return ansr.innerHTML = Math.ceil(

        // I'm going to break this down into several pieces so it's more understandable
 
        /*
        In this first calculation I needed to find out how many days would 
        complete a full month. If you look at a 30 day calendar you'll see
        there's 8 weekend days. So I subtracted 8 days from 30 days and that
        gives me a total of 22 working days. So you'll see below that I 
        divide the number of days it take to complete a project by 22. The 
        result of dividing by 22 will equal how many months are going to  be
        discounted. I then take the resulting months and multiply it by 22 
        working days in order to get my total days discounted.

        Example: dayRate(16) * (numberOfDays(130) / 22) * 22)
        130 days divided by 22 = 5 (rounded down)
        5 * 22 = 110 days that will be discounted
        110 day * $128 (using the dayRate function from above) = $14,080
        */


        ((dayRate(dailyRate.value) * (Math.floor(numberOfDays.value / 22) * 22))

        /*
        The second calculation is using the same calculation from above but
        with the discount applied. To do that I simply multiplied the discount
        by 14,080. This gives us the discount in dollars. It's then 
        subtracted from 14,080 to give us the total discounted amount.

        Example: 14,080 * 15% discount (in this case .15) = $2,112
        2,112 is then subtracted from 14,080 = $11,968 
        */

        - ((dayRate(dailyRate.value) * (Math.floor(numberOfDays.vlaue / 22) * 22)) * discountConversion)) 

        /*
        Lastly, I want to add the number of days remaining that don't complete
        a full month with a regular rate applied. The number of days discounted
        is subtracted from the total number of days needed to complete the project.
        The remaining days are then multipled by the daily rate to give us the
        amount that won't have a discount applied. It's then added to 11,968.

        Example: 130 days - 110 discounted days = 20 non-discounted days
        20 days * $128 daily rate = 2560
        11,968 + 2560 = $14,528

        $14,528 is then returned provided that the hourly rate
        is $16/hr, the project needs 130 days to complete, and the discount is 
        15%.
        */

        + (numberOfDays.value - Math.floor((numberOfDays.value / 22)) * 22) * dayRate(dailyRate.value));

        /*
        Lastly, here's the algorithm in full:
        return Math.ceil(((dayRate(dailyRate) * (Math.floor(numberOfDays / 22) * 22)) - ((dayRate(dailyRate) * (Math.floor(numberOfDays / 22) * 22)) * discount)) + (numberOfDays - Math.floor((numberOfDays / 22)) * 22) * dayRate(dailyRate))
        */
    };
  };


// Event listener for submit button
smtbtn.addEventListener('click', priceWithMonthlyDiscount)
