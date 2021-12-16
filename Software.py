Numpy = {
    'ID': 'Numpy',
    'LibraryOf': 'Python',
    'Requires': ['LinearAlgebra', 'Python'],
    'UsefulIn': 'LinearAlgebra',
}

Git = {
    'ID': 'Git',
    'Description': 'software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development.',
    'UsefulIn': ['SoftwareDevelopment', 'ProjectManagement'],
}

Docker = {
    'ID': 'Docker',
    'Description': "Docker is a containerization platform that allows you to deploy and run applications, like machine learning models. It’s becoming increasingly important that data scientists not only know how to build models but how to deploy them as well. In fact, a lot of job postings are now requiring some experience in model deployment.",
    "UsefulIn": ["ModelDeployment", "SoftwareDevelopment"],
}

Tableau = {
    'ID': 'Tableau',
    'Description': 'Data visualisation software',
    'UsefulIn': ['DataVisualisation']
}

Tensorflow = {
    'ID': 'Tensorflow',
    'Description': 'Python library for scientific computing and machine learning',
    'LibraryOf': 'Python',
    'Requires': ['Python', 'Machine Learning'],
    'UsefulIn': ['MachineLearning', "ScientificComputing", "NeuralNetworks"],
}

Keras = {
    'ID': 'Keras',
    'LibraryOf': 'Python',
    'Requires': ['MachineLearning', 'Python', "Tensorflow"],
    'UsefulIn': ['MachineLearning', "ScientificComputing", "NeuralNetworks"],
}

Software = [Numpy, Git, Docker, Tableau, Tensorflow, Keras]