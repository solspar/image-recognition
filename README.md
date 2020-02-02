## image-recognition (Sage)
# Swamphacks 2020
January 31 - February 2, 2020
Authors: Song Li, Evan Rupert, Varun Puri, Stephen Lantin

A company leader losing track of half of his workforce in the office. A software engineer whose boss might as well be a mirage. A graduate student knocking on the door of his advisor's office, only to hear nothing in return, and an intern losing his supervisor on the manufacturing floor. The inspiration for Sage arose from a frustration so small as to be nagging, yet so ubiquitous among our team members--where are our coworkers?

Sage uses facial recognition to identify people entering and leaving a building or room. It does this by first storing images of an employee on a Google Cloud Storage bucket (i.e., during a company's onboarding process). Then, as a person passes through a doorway, a camera takes an image of them, and classifies the image by name. A name, image, and timestamp are displayed on a web application hosted within a Compute Engine VM instance in the Google Cloud Platform.

See https://devpost.com/software/sage-kpmcgw for more information.
