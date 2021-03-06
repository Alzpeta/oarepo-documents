import json


def test_mapping(app):
    """Test of mapping."""
    search = app.extensions['invenio-search']
    with open(search.mappings['test-test-v1.0.0']) as f:
        data = json.load(f)
    assert data == {
        "mappings": {
            "properties": {
                "Document": {
                    "properties": {
                        "$schema": {
                            "type": "keyword"
                        },
                        "_access": {
                            "properties": {
                                "read": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "_created": {
                            "type": "date"
                        },
                        "_updated": {
                            "type": "date"
                        },
                        "abstract": {'type': 'object', 'properties':
                            {
                                'cs': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }},
                                'en': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       }
                                ,
                                'it': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       }
                                ,
                                '_': {'type': 'text',
                                      'fields': {
                                          "keywords": {
                                              "type": "keyword"
                                          }
                                      }
                                      }
                            }
                                     },
                        "alternative_abstracts": {'type': 'object', 'properties':
                            {
                                'cs': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }},
                                'en': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       }
                                ,
                                'it': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       }
                                ,
                                '_': {'type': 'text',
                                      'fields': {
                                          "keywords": {
                                              "type": "keyword"
                                          }
                                      }
                                      }
                            }
                                                  },
                        "alternative_identifiers": {
                            "properties": {
                                "material": {
                                    "type": "keyword"
                                },
                                "scheme": {
                                    "type": "keyword"
                                },
                                "value": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "alternative_titles": {'type': 'object', 'properties':
                            {
                                'cs': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }},
                                'en': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       },
                                'it': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       }
                                ,
                                '_': {'type': 'text',
                                      'fields': {
                                          "keywords": {
                                              "type": "keyword"
                                          }
                                      }
                                      }
                            }
                                               },
                        "authors": {
                            "properties": {
                                "affiliations": {
                                    "properties": {
                                        "identifiers": {
                                            "properties": {
                                                "scheme": {
                                                    "type": "keyword"
                                                },
                                                "value": {
                                                    "type": "keyword"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "name": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "alternative_names": {
                                    "type": "keyword"
                                },
                                "full_name": {
                                    "type": "text"
                                },
                                "identifiers": {
                                    "properties": {
                                        "material": {
                                            "type": "keyword"
                                        },
                                        "scheme": {
                                            "type": "keyword"
                                        },
                                        "value": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "roles": {
                                    "type": "keyword"
                                },
                                "type": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "circulation": {
                            "properties": {
                                "active_loans": {
                                    "type": "integer"
                                },
                                "can_circulate_items_count": {
                                    "type": "integer"
                                },
                                "available_items_for_loan_count": {
                                    "type": "integer"
                                },
                                "has_items_on_site": {
                                    "type": "integer"
                                },
                                "next_available_date": {
                                    "type": "date"
                                },
                                "overbooked": {
                                    "type": "boolean"
                                },
                                "overdue_loans": {
                                    "type": "integer"
                                },
                                "past_loans_count": {
                                    "type": "integer"
                                },
                                "pending_loans": {
                                    "type": "integer"
                                }
                            },
                            "type": "object"
                        },
                        "cover_metadata": {
                            "properties": {},
                            "type": "object"
                        },
                        "created_by": {
                            "properties": {
                                "type": {
                                    "type": "keyword"
                                },
                                "value": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "curated": {
                            "type": "boolean"
                        },
                        "document_type": {
                            "type": "keyword"
                        },
                        "edition": {
                            "type": "text"
                        },
                        "eitems": {
                            "properties": {
                                "hits": {
                                    "properties": {
                                        "bucket_id": {
                                            "type": "keyword"
                                        },
                                        "description": {
                                            "type": "text"
                                        },
                                        "files": {
                                            "properties": {
                                                "bucket": {
                                                    "type": "keyword"
                                                },
                                                "checksum": {
                                                    "type": "keyword"
                                                },
                                                "file_id": {
                                                    "type": "keyword"
                                                },
                                                "key": {
                                                    "type": "keyword"
                                                },
                                                "size": {
                                                    "type": "keyword"
                                                },
                                                "version_id": {
                                                    "type": "keyword"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "identifiers": {
                                            "properties": {
                                                "material": {
                                                    "type": "keyword"
                                                },
                                                "scheme": {
                                                    "type": "keyword"
                                                },
                                                "value": {
                                                    "type": "keyword"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "internal_notes": {
                                            "type": "text"
                                        },
                                        "open_access": {
                                            "type": "boolean"
                                        },
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "urls": {
                                            "properties": {
                                                "description": {
                                                    "type": "text"
                                                },
                                                "value": {
                                                    "type": "keyword"
                                                },
                                                "login_required": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "type": "object"
                                        }
                                    },
                                    "type": "object"
                                },
                                "total": {
                                    "type": "integer"
                                }
                            },
                            "type": "object"
                        },
                        "extensions": {
                            "type": "object",
                            "dynamic": False,
                            "enabled": False
                        },
                        "extensions_keywords": {
                            "type": "object",
                            "properties": {
                                "key": {"type": "keyword"},
                                "value": {"type": "keyword"}
                            }
                        },
                        "extensions_texts": {
                            "type": "object",
                            "properties": {
                                "key": {"type": "keyword"},
                                "value": {"type": "text"}
                            }
                        },
                        "extensions_longs": {
                            "type": "object",
                            "properties": {
                                "key": {"type": "keyword"},
                                "value": {"type": "long"}
                            }
                        },
                        "extensions_dates": {
                            "type": "object",
                            "properties": {
                                "key": {"type": "keyword"},
                                "value": {"type": "date"}
                            }
                        },
                        "extensions_booleans": {
                            "type": "object",
                            "properties": {
                                "key": {"type": "keyword"},
                                "value": {"type": "boolean"}
                            }
                        },
                        "identifiers": {
                            "properties": {
                                "material": {
                                    "type": "keyword"
                                },
                                "scheme": {
                                    "type": "keyword"
                                },
                                "value": {
                                    "type": "keyword"
                                },
                                "status": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "imprint": {
                            "properties": {
                                "date": {
                                    "type": "date"
                                },
                                "place": {
                                    "type": "keyword"
                                },
                                "publisher": {
                                    "type": "keyword"
                                },
                                "reprint_date": {
                                    "type": "date"
                                }
                            },
                            "type": "object"
                        },
                        "internal_notes": {
                            "properties": {
                                "field": {
                                    "type": "keyword"
                                },
                                "user": {
                                    "type": "keyword"
                                },
                                "value": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "items": {
                            "properties": {
                                "hits": {
                                    "properties": {
                                        "barcode": {
                                            "type": "keyword"
                                        },
                                        "circulation_restriction": {
                                            "type": "keyword"
                                        },
                                        "description": {
                                            "type": "text"
                                        },
                                        "internal_location": {
                                            "properties": {
                                                "location": {
                                                    "properties": {
                                                        "name": {
                                                            "type": "keyword"
                                                        }
                                                    },
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "keyword"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "internal_location_pid": {
                                            "type": "keyword"
                                        },
                                        "isbn": {
                                            "properties": {
                                                "description": {
                                                    "type": "text"
                                                },
                                                "value": {
                                                    "type": "keyword"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "medium": {
                                            "type": "keyword"
                                        },
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "shelf": {
                                            "type": "keyword"
                                        },
                                        "status": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "total": {
                                    "type": "integer"
                                }
                            },
                            "type": "object"
                        },
                        "keywords": {
                            "properties": {
                                "source": {
                                    "type": "text"
                                },
                                "value": {
                                    "type": "text"
                                }
                            },
                            "type": "object"
                        },
                        "languages": {
                            "type": "keyword"
                        },
                        "licenses": {
                            "properties": {
                                "internal_notes": {
                                    "type": "text"
                                },
                                "license": {
                                    "properties": {
                                        "id": {
                                            "type": "keyword"
                                        },
                                        "maintainer": {
                                            "type": "keyword"
                                        },
                                        "status": {
                                            "type": "keyword"
                                        },
                                        "title": {'type': 'object', 'properties':
                                            {
                                                'cs': {'type': 'text',
                                                       'fields': {
                                                           "keywords": {
                                                               "type": "keyword"
                                                           }
                                                       }},
                                                'en': {'type': 'text',
                                                       'fields': {
                                                           "keywords": {
                                                               "type": "keyword"
                                                           }
                                                       }
                                                       }
                                                ,
                                                'it': {'type': 'text',
                                                       'fields': {
                                                           "keywords": {
                                                               "type": "keyword"
                                                           }
                                                       }
                                                       }
                                                ,
                                                '_': {'type': 'text',
                                                      'fields': {
                                                          "keywords": {
                                                              "type": "keyword"
                                                          }
                                                      }
                                                      }
                                            }
                                                  },
                                        "url": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "material": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "note": {'type': 'object', 'properties':
                            {
                                'cs': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }},
                                'en': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       },
                                'it': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       }
                                ,
                                '_': {'type': 'text',
                                      'fields': {
                                          "keywords": {
                                              "type": "keyword"
                                          }
                                      }
                                      }
                            }
                                 },
                        "number_of_pages": {
                            "type": "keyword"
                        },
                        "other_authors": {
                            "type": "boolean"
                        },
                        "pid": {
                            "type": "keyword"
                        },
                        "publication_info": {
                            "properties": {
                                "artid": {
                                    "type": "keyword"
                                },
                                "journal_issue": {
                                    "type": "keyword"
                                },
                                "journal_title": {'type': 'object', 'properties':
                                    {
                                        'cs': {'type': 'text',
                                               'fields': {
                                                   "keywords": {
                                                       "type": "keyword"
                                                   }
                                               }},
                                        'en': {'type': 'text',
                                               'fields': {
                                                   "keywords": {
                                                       "type": "keyword"
                                                   }
                                               }
                                               },
                                        'it': {'type': 'text',
                                               'fields': {
                                                   "keywords": {
                                                       "type": "keyword"
                                                   }
                                               }
                                               }
                                        ,
                                        '_': {'type': 'text',
                                              'fields': {
                                                  "keywords": {
                                                      "type": "keyword"
                                                  }
                                              }
                                              }
                                    }
                                                  },
                                "journal_volume": {
                                    "type": "keyword"
                                },
                                "note": {
                                    "type": "keyword"
                                },
                                "pages": {
                                    "type": "keyword"
                                },
                                "year": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "publication_year": {
                            "type": "keyword"
                        },
                        "relation_types": {
                            "type": "keyword"
                        },
                        "relations": {
                            "properties": {
                                "next": {
                                    "properties": {
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "relation_type": {
                                            "copy_to": "relation_types",
                                            "type": "keyword"
                                        },
                                        "title": {
                                            "type": "text"
                                        }
                                    },
                                    "type": "object"
                                },
                                "previous": {
                                    "properties": {
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "relation_type": {
                                            "copy_to": "relation_types",
                                            "type": "keyword"
                                        },
                                        "title": {
                                            "type": "text"
                                        }
                                    },
                                    "type": "object"
                                },
                                "edition": {
                                    "properties": {
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "relation_type": {
                                            "copy_to": "relation_types",
                                            "type": "keyword"
                                        },
                                        "title": {
                                            "type": "text"
                                        }
                                    },
                                    "type": "object"
                                },
                                "language": {
                                    "properties": {
                                        "language": {
                                            "type": "keyword"
                                        },
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "relation_type": {
                                            "copy_to": "relation_types",
                                            "type": "keyword"
                                        },
                                        "title": {
                                            "type": "text"
                                        }
                                    },
                                    "type": "object"
                                },
                                "multipart_monograph": {
                                    "properties": {
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "relation_type": {
                                            "copy_to": "relation_types",
                                            "type": "keyword"
                                        },
                                        "title": {
                                            "type": "text"
                                        },
                                        "volume": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "other": {
                                    "properties": {
                                        "note": {
                                            "type": "keyword"
                                        },
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "relation_type": {
                                            "copy_to": "relation_types",
                                            "type": "keyword"
                                        },
                                        "title": {
                                            "type": "text"
                                        }
                                    },
                                    "type": "object"
                                },
                                "serial": {
                                    "properties": {
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "relation_type": {
                                            "copy_to": "relation_types",
                                            "type": "keyword"
                                        },
                                        "title": {
                                            "type": "text"
                                        },
                                        "volume": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                }
                            },
                            "type": "object"
                        },
                        "relations_metadata": {
                            "properties": {
                                "edition": {
                                    "properties": {
                                        "note": {
                                            "type": "keyword"
                                        },
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "language": {
                                    "properties": {
                                        "note": {
                                            "type": "keyword"
                                        },
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "multipart_monograph": {
                                    "properties": {
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "volume": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "other": {
                                    "properties": {
                                        "note": {
                                            "type": "keyword"
                                        },
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                },
                                "serial": {
                                    "properties": {
                                        "pid": {
                                            "type": "keyword"
                                        },
                                        "pid_type": {
                                            "type": "keyword"
                                        },
                                        "volume": {
                                            "type": "keyword"
                                        }
                                    },
                                    "type": "object"
                                }
                            },
                            "type": "object"
                        },
                        "restricted": {
                            "type": "boolean"
                        },
                        "source": {
                            "type": "keyword"
                        },
                        "stock": {
                            "properties": {
                                "mediums": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "subjects": {
                            "properties": {
                                "scheme": {
                                    "type": "keyword"
                                },
                                "value": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "table_of_content": {
                            "type": "text"
                        },
                        "tags": {
                            "type": "keyword"
                        },
                        "title": {'type': 'object', 'properties':
                            {
                                'cs': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }},
                                'en': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       },
                                'it': {'type': 'text',
                                       'fields': {
                                           "keywords": {
                                               "type": "keyword"
                                           }
                                       }
                                       }
                                ,
                                '_': {'type': 'text',
                                      'fields': {
                                          "keywords": {
                                              "type": "keyword"
                                          }
                                      }
                                      }
                            }
                                  },
                        "updated_by": {
                            "properties": {
                                "type": {
                                    "type": "keyword"
                                },
                                "value": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        },
                        "urls": {
                            "properties": {
                                "description": {'type': 'object', 'properties':
                                    {
                                        'cs': {'type': 'text',
                                               'fields': {
                                                   "keywords": {
                                                       "type": "keyword"
                                                   }
                                               }},
                                        'en': {'type': 'text',
                                               'fields': {
                                                   "keywords": {
                                                       "type": "keyword"
                                                   }
                                               }
                                               },
                                        'it': {'type': 'text',
                                               'fields': {
                                                   "keywords": {
                                                       "type": "keyword"
                                                   }
                                               }
                                               }
                                        ,
                                        '_': {'type': 'text',
                                              'fields': {
                                                  "keywords": {
                                                      "type": "keyword"
                                                  }
                                              }
                                              }
                                    }
                                                },
                                "value": {
                                    "type": "keyword"
                                }
                            },
                            "type": "object"
                        }
                    }
                }
            }
        }}
