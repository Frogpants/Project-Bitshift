
// The code is split up to easily understand for new programmers to 3D math and calculations. It is complete possible to compact this code
// into a simpler version, if you'd prefer that you can do that on your own.

// This javascript file has helpful comments to teach you how to do simple 3D math calculations in js.
// If you'd like a step by step tutorial, follow this link: https://pages.opencodingsociety.com/navigation/documentation/tutorial/intro


const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

const halfWidth = canvas.width / 2;
const halfHeight = canvas.height / 2;


const vector = {
    x: 0,
    y: 0,
    z: 0
};


const camera = {
    x: 0,
    y: 0,
    z: 0,
    FOV: 90,
    direction : {
        x: 0,
        y: 0,
        z: 0
    }
};


const focalLength = 1 / Math.tan(toRadians(camera.FOV) / 2);


function toRadians(val) {

    return val * (Math.PI / 180)
};

function Vector3(x,y,z) {

    vector.x = x;
    vector.y = y;
    vector.z = z;
};



function translate(x,y,z) {

    const tempX = x - camera.x;
    const tempY = y - camera.y;
    const tempZ = z - camera.z;

    Vector3(tempX, tempY, tempZ);
};



function rotateX(x,y,z) {

    const angle = toRadians(camera.direction.x);

    const tempX = x * Math.cos(angle) - z * Math.sin(angle);
    const tempZ = x * Math.sin(angle) + z * Math.cos(angle);

    Vector3(tempX, y, tempZ);
};



function rotateY(x,y,z) {

    const angle = toRadians(camera.direction.y);

    const tempY = y * Math.cos(angle) - z * Math.sin(angle);
    const tempZ = y * Math.sin(angle) + z * Math.cos(angle);

    Vector3(x, tempY, tempZ);
};



function rotateZ(x,y,z) {

    const angle = toRadians(camera.direction.z);

    const tempX = x * Math.cos(angle) - y * Math.sin(angle);
    const tempY = x * Math.sin(angle) + y * Math.cos(angle);

    Vector3(tempX, tempY, z);
};



function project3DTo2D(x,y,z) {

    const tempX = halfWidth + halfWidth * focalLength * (x / z);
    const tempY = halfHeight + halfWidth * focalLength * (y / z);

    return {x: tempX, y: tempY};
};



function goTo(x,y,z) {
    translate(x,y,z);

    rotateX(vector.x, vector.y, vector.z);
    rotateY(vector.x, vector.y, vector.z);
    rotateZ(vector.x, vector.y, vector.z);

    return project3DTo2D(vector.x, vector.y, vector.z);
};


// Rendering

// Rendering can be very simple be drawing lines that connect each point of an object
// This form is called wireframe rendering


// We can use distance between each point from the camera to add depth for the line widths

function distanceTo(x,y,z) {
    const tempX = x - camera.x;
    const tempY = y - camera.y;
    const tempZ = z - camera.z;
    return Math.sqrt(tempX * tempX + tempY * tempY + tempZ * tempZ); // Distance formula = sqrt(x^2 + y^2 + z^2)
};



function drawLine(x1,y1,x2,y2) {
    // Initializes line segment
    ctx.beginPath();

    // Move the pen to starting point (x1, y1)
    ctx.moveTo(x1, y1);

    // Draw a line to (x2, y2)
    ctx.lineTo(x2, y2);

    // Draw the line
    ctx.stroke();
};


