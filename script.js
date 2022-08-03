/*
---------------------------------------Description--------------------------------------

This is a discount calculator created for a freelance worker who wants to calculate 
his rates given 8 hour days with a discount if the project spans several months. He 
wants to give a discount for every full month worked and any remaining days that don't
equal a full month will be billed at his regular rate.

 ---------------------------------------------------------------------------------------
*/

// This function calculates a daily income by simply multiplying an hourly pay rate by 8 hours.
export function dayRate(ratePerHour) {
    return ratePerHour * 8
  }

/* 
You'll see in the next function that it takes in 3 parameters. 
- The ratePerHour (which can be used with the dayRate() function above) 
- numDay - number of days needed to complete the project
- discount - the percent discount applied for every month of work
*/ 

export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {

    // If a discount isn't being applied it can still calculate a regular rate
    // with the below 'if' statement

    if (discount <= 0) {
      return dayRate(ratePerHour) * Math.floor(numDays)
    } else {
      return Math.ceil(

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

        Example: dayRate(16) * (numDays(130) / 22) * 22)
        130 days divided by 22 = 5 (rounded down)
        5 * 22 = 110 days that will be discounted
        110 day * $128 (using the dayRate function from above) = $14,080
        */

        ((dayRate(ratePerHour) * (Math.floor(numDays / 22) * 22))

        /*
        The second calculation is using the same calculation from above but
        with the discount applied. To do that I simply multiplied the discount
        by 14,080. This gives us the discount in dollars. It's then 
        subtracted from 14,080 to give us the total discounted amount.

        Example: 14,080 * 15% discount (in this case .15) = $2,112
        2,112 is then subtracted from 14,080 = $11,968 
        */

        - ((dayRate(ratePerHour) * (Math.floor(numDays / 22) * 22)) * discount)) 

        /*
        Lastly, I want to add the number of days remaining that don't complete
        a full month with a regular rate applied. The number of days discount
        is subtracted from the total number of days needed to complete the project.
        The remaining days are then multipled by the daily rate to give us the
        amount that won't have a discount applied. It's then added to 11,968.

        Example: 130 days - 110 days = 20 days
        20 days * $128 = 2560
        11,968 + 2560 = $14,528

        $14,528 is then returned as the solution provided that the hourly rate
        is $16/hr, the project needs 130 days to complet, and the discount is 
        15%.
        */
        + (numDays - Math.floor((numDays / 22)) * 22) * dayRate(ratePerHour))

        /*
        Lastly, here's the algorithm in full:
        return Math.ceil(((dayRate(ratePerHour) * (Math.floor(numDays / 22) * 22)) - ((dayRate(ratePerHour) * (Math.floor(numDays / 22) * 22)) * discount)) + (numDays - Math.floor((numDays / 22)) * 22) * dayRate(ratePerHour))
        */
    }
  }
