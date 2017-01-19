from __future__ import absolute_import

"""
{
  "id": 298,
  "rev": 1,
  "fields": {
    "System.AreaPath": "Fabrikam-Fiber-Git",
    "System.TeamProject": "Fabrikam-Fiber-Git",
    "System.IterationPath": "Fabrikam-Fiber-Git",
    "System.WorkItemType": "Task",
    "System.State": "To Do",
    "System.Reason": "New task",
    "System.CreatedDate": "2014-12-29T20:49:21.21Z",
    "System.CreatedBy": "Jamal Hartnett <fabrikamfiber4@hotmail.com>",
    "System.ChangedDate": "2014-12-29T20:49:21.21Z",
    "System.ChangedBy": "Jamal Hartnett <fabrikamfiber4@hotmail.com>",
    "System.Title": "JavaScript implementation for Microsoft Account"
  },
  "_links": {
    "self": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/298"
    },
    "workItemUpdates": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/298/updates"
    },
    "workItemRevisions": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/298/revisions"
    },
    "workItemHistory": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/298/history"
    },
    "html": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/web/wi.aspx?pcguid=d81542e4-cdfa-4333-b082-1ae2d6c3ad16&id=298"
    },
    "workItemType": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c/_apis/wit/workItemTypes/Task"
    },
    "fields": {
      "href": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/fields"
    }
  },
  "url": "https://fabrikam-fiber-inc.visualstudio.com/DefaultCollection/_apis/wit/workItems/298"
}
"""

class VisualStudioClient(object):
    def create_work_item(self, title, description):
        # PATCH https://sentryio.visualstudio.com/DefaultCollection/MyFirstProject/_apis/wit/workitems/$Task?api-version=1.0
        json = [
          {
            'op': 'add',
            'path': '/fields/System.Title',
            'value': title,
          },
          {
            'op': 'add',
            'path': '/fields/System.Description',
            'value': description
          },
          {
            'op': 'add',
            'path': '/fields/System.History',
            'value': 'Jim has the most context around this.'
          },
        ]
