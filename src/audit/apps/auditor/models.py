from utils.loading import is_model_registered
from .abstract_models import (AbstractAnalyzer,
                              AbstractAnalyzerLog)

__all__ = []


if not is_model_registered('auditor', 'Analyzer'):
    class Analyzer(AbstractAnalyzer):
        pass

    __all__.append('Analyzer')


if not is_model_registered('auditor', 'AnalyzerLog'):
    class AnalyzerLog(AbstractAnalyzerLog):
        pass

    __all__.append('AnalyzerLog')
