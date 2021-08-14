$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: true,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
/*the belwo plus cart is a class in a addtocart.html on that class we applied a clickfunction */
$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString(); /*convert id integer into string */
    var eml = this.parentNode.children[2]
    /* nwo we need to send the id to the server for thatt using ajax we can send */
    $.ajax({
        type:'GET',
        url :"/pluscart", /*on this url belwo data will send */
        data:{
            prod_id:id 
        },
        success:function(data){
            eml.innerText = data.quantity
            /* now pass this data amt to addtocart.html*/
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount

        }
        }
    )
})

/*the belwo minus cart is a class in a addtocart.html on that class we applied a clickfunction */

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString(); /*convert id integer into string */
    var eml = this.parentNode.children[2]
    /* nwo we need to send the id to the server for thatt using ajax we can send */
    $.ajax({
        type:'GET',
        url :"/minuscart", /*on this url belwo data will send */
        data:{
            prod_id:id 
        },
        success:function(data){
            eml.innerText = data.quantity
            /* now pass this data amt to addtocart.html*/
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount

        }
        }
    )
})
/*the belwo remove cart is a class in a addtocart.html on that class we applied a clickfunction */

$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString(); /*convert id integer into string */
    var eml = this 
     /* nwo we need to send the id to the server for thatt using ajax we can send */
    $.ajax({
        type:'GET',
        url :"/removecart", /*on this url belwo data will send */
        data:{
            prod_id:id 
        },
        success:function(data){
            console.log("Delete")
            /* now pass this data amt to addtocart.html*/
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()              /* to remove the item need to go inside div/div/div/div*/

        }
        }
    )
})