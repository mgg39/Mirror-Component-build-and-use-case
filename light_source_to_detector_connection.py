mport math
from sequence.kernel.timeline import Timeline
from sequence.kernel.event import Event
from sequence.kernel.process import Process
from sequence.components.light_source import LightSource
from sequence.components.light_source import polarization
from sequence.components.optical_channel import QuantumChannel
from sequence.components.detector import Detector
from sequence.topology.node import Node

NUM_TRIALS = 1000
FREQUENCY = 1e3

class Counter():
    def __init__(self):
        self.count = 0

    def trigger(self, detector, info):
        self.count += 1

class ReceiverNode(Node):
    def __init__(self, name, timeline):
        super().__init__(name, timeline)
        self.detector = Detector(name + ".detector", tl, efficiency=1)
        self.detector.owner = self

    def receive_qubit(self, src, qubit):
        if not qubit.is_null:
            self.detector.get()


if __name__ == "__main__":
    runtime = 10e12 
    tl = Timeline(runtime)

    # nodes and hardware
    node1 = SenderNode("node1", tl)
    node2 = ReceiverNode("node2", tl)

    qc = QuantumChannel("qc", tl, attenuation=0, distance=1e3)
    qc.set_ends(node1, node2)

    # counter
    counter = Counter()
    node2.detector.attach(counter)

    # schedule events
    time_bin = int(1e12 / FREQUENCY)
    
    #Process -> for memory not light source
    process1 = Process(node1,light_source, "emit", [[((1+0j),0j)], ["node2"]])

event1=Event(0,process1)
    tl.init()
    tl.run()

    print("percent measured: {}%".format(100 * counter.count / NUM_TRIALS))
