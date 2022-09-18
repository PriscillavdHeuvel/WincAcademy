# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"


# Add your code after this line
def main():
    # Create a greeting
    print(greet(1))
    print(greet("Bob", "What's up, <name>!"))

    # Calculate force on an object on a specific celestial body
    print(force(2000, "Jupiter"))
    print(force(2000, "test"))
    print(force("test", "Earth"))
    print(force("test", "test"))

    # Calculate the gravitational pull between two objects
    print(pull(300, 0.2, 500))
    print(pull("test", 0.2, 500))


# Part 1 - Greet template
def greet(name, greeting_template="Hello, <name>!"):
    """Create a greeting.

    Arguments:
    name -- the name you want to include in the greeting.
    greeting_template -- a sentence you want to use as a greeting. You put
    <name> as a placeholder where you want the name to be (default=Hello,
    <name>!).
    """
    # Check if arguments are strings
    if type(name) == str and type(greeting_template) == str:
        # Replace <name> with the name argument
        greeting = greeting_template.replace("<name>", name)
        return greeting

    else:
        problem_message = "Not all arguments are strings. Please try again."
        return problem_message


# Part 2 - Force
def force(mass, body="earth"):
    """Calculate the force on an object with a certain mass on a specific
    celestial body.

    Arguments:
    mass -- the mass of an object in kg.
    body -- the name of a celestial body. Options are: Jupiter, Neptune,
    Saturn, Earth, Uranus, Venus, Mars, Mercury, Pluto, the moon or the
    sun (default=earth).
    """
    # Create a dictionary with the surface gravity of the planets and the sun
    surface_gravity_bodies = {
        "sun": 274.0,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }

    # Change the body argument to lower case if it's a string
    if type(body) == str:
        lower_case_body = body.lower()

        # Convert the mass argument to a float and calculate the force. If a
        # ValueError occurs, print message to enter a valid value for mass
        try:
            mass_float = float(mass)

            # Check if celestial body is present in dictionary
            if surface_gravity_bodies.get(lower_case_body) is not None:
                # Calculate the force
                force = mass_float * surface_gravity_bodies.get(lower_case_body)
                return force

            # If celestial body is not present in dictionary, print message to
            # enter a valid celestial body
            else:
                problem_message = "Please enter a valid celestial body."
                return problem_message

        # If mass argument is not convertable to a float
        except ValueError:
            problem_message = "The specified mass can't be converted to a float. Please enter a valid value."
            return problem_message

    # If body argument is not a string, print message to enter a string value
    else:
        problem_message = "Please enter a string as a celestial body"
        return problem_message


# Part 3 - Gravity
def pull(m1, m2, d):
    """Calculate the gravitational pull between two objects.

    Arguments:
    m1 -- the mass in kg of object 1.
    m2 -- the mass in kg of object 2.
    d -- the distance in meters between the two objects.
    """
    # Convert the arguments to floats. If a ValueError occurs, print
    # message to enter valid values
    try:
        mass_object1 = float(m1)
        mass_object2 = float(m2)
        distance = float(d)
        gravitational_constant = 6.674e-11

        # Calculate the gravitational pull between the two objects
        pull = gravitational_constant * (
            (mass_object1 * mass_object2) / (distance**2)
        )
        return pull

    # If arguments are not convertable to floats
    except ValueError:
        problem_message = "One or more of the specified values can't be converted to a float. Please enter valid values."
        return problem_message


if __name__ == "__main__":
    main()
