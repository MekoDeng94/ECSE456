import nltk
from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from runner.console_monochrome import Console

logger = Console()

nltk.download('vader_lexicon')

#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# using https://www.forbes.com/sites/katinastefanova/2015/12/21/50-words-in-earnings-reports-that-mean-a-plumeting-stock-price/#33f0fc556ac9
new_words = {
    'recalculate': -4, 'testify': -4, 'questionable': -4, 'impeded': -4, 'exacerbate': -4, 'overstatement': -4, 'slander': -4, 'nonperforming': -4, 'unfounded': -4, 'worst': -4, 'illicit': -4, 'renegotiate': -4, 'manipulate': -4, 'disturbing': -4, 'circumvent': -4, 'prejudiced': -4, 'apparently': -4, 'frivolous': -4, 'reject': -4, 'protested': -4, 'rejects': -4, 'downsized': -4, 'grievance': -4, 'refile': -4, 'dissenting': -4, 'foreclosed': -4, 'gratuitous': -4, 'unpredicted': -4, 'misapplication': -4, 'closeout': -4, 'collaborates': -4, 'obligee': -4, 'dissenters': -4, 'forego': -4, 'writs': -4, 'pledgors': -4, 'precipitated': -4, 'idled': -4, 'suggests': -4, 'bailee': -4, 'friendly': -4, 'arbitral': -4, 'breakthroughs': -4, 'favoring': -4, 'certiorari': -4, 'persists': -4, 'adjournments': -4, 'ignoring': -4,
    'unmatched': 4, 'outperform': 4, 'voided': 4, 'confident': 4, 'rewarded': 4, 'prosperity': 4, 'discrepancy': 4, 'rectification': 4, 'critically': 4, 'forfeitable': 4, 'arbitrary': 4, 'turmoil': 4, 'imbalance': 4, 'progresses': 4, 'antecedent': 4, 'overcharged': 4, 'duress': 4, 'manipulation': 4, 'distressed': 4, 'dissolutions': 4, 'hazard': 4, 'expropriation': 4, 'understate': 4, 'unfit': 4, 'pleadings': 4, 'investigated': 4, 'sometime': 4, 'encroachment': 4, 'misstate': 4, 'mutandis': 4, 'defraud': 4, 'undefined': 4, 'delisting': 4, 'forfeits': 4, 'uncovers': 4, 'malpractice': 4, 'presumes': 4, 'grantors': 4, 'collapsing': 4, 'falsely': 4, 'unsound': 4, 'rejections': 4, 'whereabouts': 4, 'damaging': 4, 'reassignment': 4, 'distracting': 4, 'disapproved': 4, 'stagnant': 4, 'predeceases': 4, 'unsafe': 4,
    'improves': 0, 'gain': 0, 'fluctuation': 0, 'discontinue': 0, 'statutes': 0, 'thereunto': 0, 'risky': 0, 'fluctuates': 0, 'subrogation': 0, 'negatively': 0, 'lose': 0, 'attorney': 0, 'revised': 0, 'could': 0, 'exposure': 0, 'dependent': 0, 'will': 0, 'contracts': 0, 'failure': 0, 'risk': 0, 'easily': 0, 'proficiency': 0, 'supersedes': 0, 'accession': 0, 'duly': 0, 'may': 0, 'remedied': 0, 'variable': 0, 'unenforceable': 0, 'risks': 0, 'unresolved': 0, 'variations': 0, 'courts': 0, 'problem': 0, 'varied': 0, 'hereby': 0, 'predict': 0, 'favorable': 0, 'vulnerability': 0, 'claims': 0, 'alteration': 0, 'discontinuing': 0, 'bankruptcy': 0, 'depending': 0, 'attaining': 0, 'omissions': 0, 'correcting': 0,
    'rising':4,'rise':4,'well positioned':4,'grow':4,'growth':4
}


analyzer = SentimentIntensityAnalyzer()

analyzer.lexicon.update(new_words)

def get_vader_sentiment(text):
    Article_sentences = []
    return_value = 0
    try:
        Article_sentences = [sentence + '.' for sentence in text.replace('\n','').split('.') if 'AMD' in sentence]
        total_score = 0

        for sentence in Article_sentences:
            scores = analyzer.polarity_scores(sentence)
            total_score += scores['compound']

        return_value = repr(total_score/len(Article_sentences))
        
    except Exception as e:
        pass

    return float(return_value)