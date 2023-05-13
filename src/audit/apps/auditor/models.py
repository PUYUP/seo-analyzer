from utils.loading import is_model_registered
from .abstract_models import (AbstractAnalyzer,
                              AbstractAnalyzerLog,
                              AbstractNews)

__all__ = []


if not is_model_registered('auditor', 'Analyzer'):
    class Analyzer(AbstractAnalyzer):
        pass

    __all__.append('Analyzer')


if not is_model_registered('auditor', 'AnalyzerLog'):
    class AnalyzerLog(AbstractAnalyzerLog):
        pass

    __all__.append('AnalyzerLog')


if not is_model_registered('auditor', 'News'):
    class News(AbstractNews):
        pass

    __all__.append('News')
