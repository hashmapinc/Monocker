'use strict';

//TODO: implement actual H2 db instead of this dummy array.
var models = ["model_0"];

/** Gets all models registered in the last minute from H2
 *  
 *  This function returns an array of model objects from
 *  all models registered in H2 in the last minute. These
 *  models are considered 'fresh' and able to responde to
 *  requests.
 */
function getModels (req, res) {
  //TODO: Get models for real
  res.json(models);
}

/** Registers 1 or more models into the H2 registry
 *  
 *  This function saves monocker-model metadata to the H2
 *  registry so clients can find and utlize monocker-model services. 
 */
function registerModels (req, res) {
  //TODO: Save models for real
  models.push(req.swagger.params.model_name.value);
  res.json({success: 1, description: "Models added"});
}

//export handlers
module.exports = {
  getModels:        getModels,
  registerModels:   registerModels
};