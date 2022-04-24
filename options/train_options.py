from .base_options import BaseOptions
import os

class TrainOptions(BaseOptions):
    """This class includes training options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)
        parser.add_argument('--useRestore', type=bool, default=False, help='whether restore or not')
        parser.add_argument('--batch_size', type=int, default=1, help='input batch size') #changed to 1 to be able to run with weak gpu
        parser.add_argument('--lr', type=float, default=0.0001, help='initial learning rate for adam')
        parser.add_argument('--max_iteration', type=int, default=20001, help='iterations for batch_size samples')
        parser.add_argument('--print_info_freq', type=int, default=500, help='frequency of printing train result')
        parser.add_argument('--mode', type=str, default='train')

        return parser
