'use strict';

var SwaggerExpress = require('swagger-express-mw')
  , app = require('express')();

module.exports = app; // for testing

var config = {
  appRoot: __dirname // required config
};

SwaggerExpress.create(config, function(err, swaggerExpress) {
  if (err) { throw err; }

  // install middleware
  swaggerExpress.register(app);

  var port = 10010;
  app.listen(port);

  console.log('listening on port ' + port);   
});
