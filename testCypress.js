describe('Player Tests', function() {

  //Click on element to enter video player
it ('Clicks on element', function() {
  //Arrange
  cy.visit('https://player.smartzer.com/v/5695094313189376')
//act
cy.contains('SHOP THE VIDEO')
//Assert
  cy.url().should('include', 'https://player.smartzer.com')
})

//Access the interactive ad
it ('Can access interactive video ad', function() {
  //Arrange
  cy.visit('https://player.smartzer.com/v/5695094313189376')

  //act
cy.get('button[aria-label="Click to play the video"]').click()
cy.wait(1000)

//Assert interactive ad is loaded and shoes item drawer at side
cy.wait(1000)
cy.get('button[aria-label="Open panel to see all options"]').should('be.visible')

})

it ('Can pull out the dropdown sidebar', function() {
  //Arrange
  cy.visit('https://player.smartzer.com/v/5695094313189376')
//act
cy.get('button[aria-label="Click to play the video"]').click()
cy.wait(1000)
cy.get('button[aria-label="Open panel to see all options"]').click()
cy.wait(1000)

//Assert
//check that the all the products are available in the list
cy.get('img[alt="Ernest armchair"]').should('be.visible')
cy.get('img[alt="Lonna stool 44cm"]').should('be.visible')
cy.get('img[alt="Ernest table"]').should('be.visible')

})

it ('Can close the pull out drawer', function() {
  //Arrange
  cy.visit('https://player.smartzer.com/v/5695094313189376')
//act
cy.get('button[aria-label="Click to play the video"]').click()
cy.wait(1000)
cy.get('button[aria-label="Open panel to see all options"]').click()
cy.wait(1000)
cy.get('button[aria-label="Close panel"]').click()
cy.wait(1000)

//Assert
//check that the all the products are not available in the list
cy.get('img[alt="Ernest armchair"]').should('not.be.visible')


})



})

//