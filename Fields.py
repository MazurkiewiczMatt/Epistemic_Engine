

LinearAlgebra = {
    'ID': 'LinearAlgebra',
    'BranchOf': 'Mathematics',
    'UsefulIn': ['MachineLearning'],
}

SignalProcessing = {
    'ID': 'SignalProcessing',
    'BranchOf': 'ElectricalEngineering',
    'UsefulIn': ['Communications', 'Vibrations', 'Sounds'],
    'Requires': 'FourierTransform',
}

FourierTransform = {
    'ID': 'FourierTransform',
    'BranchOf': 'Mathematics',
    'UsefulIn': ['Convolution', 'SignalProcessing'],
}

Convolution = {
    'ID': 'Convolution',
    'BranchOf': 'Mathematics',
    'UsefulIn': ['Probability', 'ControlTheory', 'SignalProcessing'],
}

ControlTheory = {
    'ID': 'ControlTheory',
    'BranchOf': 'Engineering',
    'UsefulIn': ['Robotics']
}


ElectricalEngineering = {
    'ID': 'ElectricalEngineering',
    'BranchOf': 'Engineering',
}

SoftwareDevelopment = {
    'ID': 'SoftwareDevelopment',
    'BranchOf': 'Engineering',
}

ComputerScience = {
    'ID': 'ComputerScience',
    'BranchOf': 'Science',
    'UsefulIn': 'SoftwareDevelopment'
}

Fields = [LinearAlgebra, SignalProcessing, FourierTransform, Convolution, ControlTheory, ElectricalEngineering, SoftwareDevelopment, ComputerScience]
