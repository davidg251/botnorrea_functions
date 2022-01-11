/**
 * Responds to a GET request with "Hello World!". Forbids a PUT request.
 *
 * @example
 * gcloud functions call helloHttp
 *
 * @param {Object} req Cloud Function request context.
 * @param {Object} res Cloud Function response context.
 */
 exports.helloHttp = (req, res) => {
    switch (req.method) {
      case 'GET':
        res.status(200).send('Hello World!');
        break;
      case 'PUT':
        res.status(403).send('Forbidden!');
        break;
      default:
        res.status(405).send({error: 'Something blew up!'});
        break;
    }
  };